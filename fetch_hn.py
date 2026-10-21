import urllib.request, json, datetime, sys

now = datetime.datetime.now(datetime.timezone.utc)
cutoff = now - datetime.timedelta(hours=72)
print(f"Now: {now.isoformat()}")
print(f"Cutoff: {cutoff.isoformat()}")

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())

# 1) Top stories from Firebase API, filter to last 72h
ids = fetch_json("https://hacker-news.firebaseio.com/v0/topstories.json")[:150]
top_stories = []
for sid in ids:
    try:
        item = fetch_json(f"https://hacker-news.firebaseio.com/v0/item/{sid}.json")
        if item.get("type") == "story":
            ts = item.get("time", 0)
            dt = datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc)
            if dt > cutoff:
                top_stories.append({
                    "id": str(sid),
                    "title": item.get("title"),
                    "url": item.get("url", ""),
                    "score": item.get("score", 0),
                    "time": dt.isoformat(),
                    "desc": item.get("descendants", 0),
                    "type": "top",
                })
    except Exception:
        pass

print(f"\n=== TOP STORIES (72h): {len(top_stories)} ===")
for s in sorted(top_stories, key=lambda x: x["score"], reverse=True):
    print(json.dumps(s))

# 2) Algolia queries across 5 domains - fetch and filter client-side
algolia_queries = {
    "AI/ML": ["AI", "machine learning", "LLM", "OpenAI", "model"],
    "Cloud/AWS": ["AWS", "cloud", "Azure", "GCP", "serverless"],
    "Cybersecurity": ["security", "vulnerability", "CVE", "exploit", "encryption"],
    "DevOps/Infrastructure": ["kubernetes", "docker", "terraform", "devops", "infrastructure"],
    "Developer tools/Emerging": ["Rust", "programming language", "compiler", "editor", "IDE"],
}

all_hits = {}
for area, terms in algolia_queries.items():
    all_hits[area] = []
    seen = set()
    for term in terms:
        try:
            from urllib.parse import quote
            url = f"https://hn.algolia.com/api/v1/search?query={quote(term)}&tags=story&hitsPerPage=100"
            data = fetch_json(url)
            for h in data.get("hits", []):
                created = h.get("created_at", "")
                try:
                    dt = datetime.datetime.fromisoformat(created.replace("Z", "+00:00"))
                except ValueError:
                    continue
                if dt > cutoff and h.get("objectID") not in seen:
                    seen.add(h.get("objectID"))
                    all_hits[area].append({
                        "id": str(h.get("objectID")),
                        "title": h.get("title"),
                        "url": h.get("url", ""),
                        "points": h.get("points", 0),
                        "time": created,
                        "area": area,
                        "term": term,
                    })
        except Exception as e:
            print(f"  [warn] {area}/{term}: {e}", file=sys.stderr)

    print(f"\n=== {area} (72h): {len(all_hits[area])} ===")
    for h in sorted(all_hits[area], key=lambda x: x["points"], reverse=True)[:15]:
        print(json.dumps(h))

with open("hn_recent.json", "w") as f:
    json.dump({"top_stories": top_stories, "by_area": all_hits,
               "generated": now.isoformat()}, f, indent=2)
print("\nSaved hn_recent.json")

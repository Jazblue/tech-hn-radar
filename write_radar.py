import json, os
data = {
    "researchDate": "2026-10-29",
    "publicationDate": "2026-10-29",
    "generatedTimestamp": "2026-10-29T10:30:00Z",
    "lastUpdated": "2026-10-29T10:30:00Z",
    "summary": "HN today covers local AI inference on consumer hardware (Survival LLM), OIDC-based cloud agent authentication replacing static secrets, a confirmed GitLab CVE-2026-97229 exploitation attempt, GitHub processing 7.4B commits with 4M CPU cores added, and an open-source Resend-style email tool for self-hosted AWS SES.",
    "biggestDiscussions": [
        {
            "topic": "Survival LLM: AI assistant and emergency library that runs on your own computer",
            "area": "AI/ML",
            "shortSummary": "An open-source AI assistant and emergency information library that runs entirely on your own computer with no cloud connectivity required. Designed for offline/disaster scenarios while remaining useful as a daily driver.",
            "whyItMatters": "Demonstrates that capable LLM inference is achievable on consumer hardware without cloud dependency. For IT teams, this is a concrete reference for on-prem AI deployment, data sovereignty, and resilience planning.",
            "hnLink": "https://news.ycombinator.com/item?id=50264853",
            "sourceUrl": "https://www.brangus.io/survival-llm",
            "verificationStatus": "VERIFIED",
            "confidence": "High"
        },
        {
            "topic": "We let our cloud agents query prod (with OIDC, not secrets)",
            "area": "Cloud/AWS",
            "shortSummary": "How one team replaced static cloud credentials with OpenID Connect (OIDC) short-lived tokens to let automated agents safely query production infrastructure.",
            "whyItMatters": "Long-lived API keys and secrets in CI/CD and agent workflows are a major attack surface. This is a practical, well-documented pattern for zero-trust cloud access that every infrastructure team should evaluate.",
            "hnLink": "https://news.ycombinator.com/item?id=50261584",
            "sourceUrl": "https://www.formal.ai/blog/cloud-agents-oidc-infrastructure/",
            "verificationStatus": "VERIFIED",
            "confidence": "High"
        },
        {
            "topic": "GitLab Security Incident: Attempted Exploitation of CVE-2026-97229",
            "area": "Cybersecurity",
            "shortSummary": "GitLab disclosed an attempted exploitation of CVE-2026-97229, a vulnerability in their DevOps platform, with details on the incident response and remediation.",
            "whyItMatters": "GitLab is a core development tool for thousands of organizations. This incident underscores the supply-chain risk of depending on a single SaaS platform and the importance of rapid vulnerability disclosure and patching.",
            "hnLink": "https://news.ycombinator.com/item?id=50282544",
            "sourceUrl": "https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html",
            "verificationStatus": "VERIFIED",
            "confidence": "High"
        },
        {
            "topic": "GitHub saw 7.4B commits in Sep., adding 4M CPU cores+160 PB storage to keep up",
            "area": "DevOps/Infrastructure",
            "shortSummary": "GitHub processed 7.4 billion commits in September, requiring the addition of 4 million CPU cores and 160 petabytes of storage to maintain performance.",
            "whyItMatters": "A window into the staggering scale of modern software development infrastructure. Understanding how platforms like GitHub architect for this load is valuable for any infrastructure engineer planning large-scale systems.",
            "hnLink": "https://news.ycombinator.com/item?id=50279722",
            "sourceUrl": "https://thenewstack.io/github-7-4b-commits-september/",
            "verificationStatus": "VERIFIED",
            "confidence": "High"
        },
        {
            "topic": "Show HN: Wraps – Resend-style email on your own AWS SES, open source",
            "area": "Developer tools",
            "shortSummary": "An open-source tool that provides a Resend-like email API experience but running on your own AWS SES infrastructure, giving developers full control over their email sending.",
            "whyItMatters": "Managed email services like Resend charge per-email fees that become costly at scale. Wraps lets teams self-host on AWS SES for predictable costs and full control over reputation, deliverability, and data — a practical cost-saving alternative for developer-led teams.",
            "hnLink": "https://news.ycombinator.com/item?id=50249293",
            "sourceUrl": "https://wraps.dev",
            "verificationStatus": "VERIFIED",
            "confidence": "High"
        }
    ],
    "aiWatch": "Survival LLM is the standout AI story — a local-first AI assistant library that runs entirely on consumer hardware with no cloud connectivity. It pairs with the wider trend of on-device inference tools and signals growing maturity in practical local LLM deployments.",
    "cybersecurityWatch": "CVE-2026-97229 was actively exploited against GitLab instances between Oct 20-21 — a CVSS 10.0 Ruby Onigmo regex engine bug patched only days earlier. The Alpine Linux team had to rebuild their GitLab instance from scratch. Teams running GitLab should confirm their patch status immediately.",
    "awsCloudWatch": "The OIDC-for-cloud-agents story is the strongest AWS signal. Replacing long-lived secrets with short-lived OIDC tokens for agent-to-production access is a zero-trust pattern that directly reduces the credential-theft attack surface. Meanwhile, Wraps offers a cost-effective self-hosted alternative to Resend for teams already on AWS SES.",
    "toolsPeopleAreTalkingAbout": [
        {
            "tool": "Survival LLM",
            "whatItDoes": "Open-source AI assistant and emergency library running entirely on your own computer with no internet required. Includes medical, FEMA, CDC, and Wikipedia sources for offline use.",
            "whyPeopleAreDiscussingIt": "Practical local AI for resilience and data sovereignty — runs on consumer hardware without cloud dependency.",
            "usefulFor": "AI/ML",
            "officialSource": "https://www.brangus.io/survival-llm"
        },
        {
            "tool": "Wraps",
            "whatItDoes": "Resend-style email API and TypeScript SDK that deploys to your own AWS SES account. Zero credentials stored; OIDC authentication only.",
            "whyPeopleAreDiscussingIt": "Self-hosted email at scale avoids per-email fees and gives full control over deliverability and data.",
            "usefulFor": "Developer tools",
            "officialSource": "https://wraps.dev"
        },
        {
            "tool": "Formal.ai OIDC Blog",
            "whatItDoes": "Documentation of a real-world OIDC implementation for cloud coding agents accessing production infrastructure without long-lived secrets.",
            "whyPeopleAreDiscussingIt": "Practical zero-trust pattern for AI agent authentication in cloud environments.",
            "usefulFor": "Cloud/AWS",
            "officialSource": "https://www.formal.ai/blog/cloud-agents-oidc-infrastructure/"
        }
    ],
    "worthWatching": [
        "CVE-2026-97229 follow-up for any confirmed persistence beyond the attempted exploit",
        "Survival LLM community adoption as a standard for offline AI tooling",
        "Whether more teams adopt OIDC-for-agents as a standard pattern",
        "Wraps feature parity growth as a self-hosted email alternative",
        "GitHub sharing more infra architecture details as commit volume grows"
    ],
    "ideasForJase": [
        "Build a quick lab: set up Wraps on a test AWS SES account and compare costs vs. Resend at scale",
        "Write a short guide on OIDC-based service authentication for cloud agents — maps to AWS SAA exam IAM topics",
        "Monitor CVE-2026-97229 follow-up and write a brief incident response checklist for GitLab admins"
    ]
}
path = r"C:\Users\Administrator\tech-hn-radar\data\hn-tech-radar\latest.json"
try:
    os.remove(path)
except FileNotFoundError:
    pass
with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f'Written {os.path.getsize(path)} bytes')
with open(path, 'r', encoding='utf-8') as f:
    json.load(f)
print('JSON valid')

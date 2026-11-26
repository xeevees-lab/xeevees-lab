# -----------------------------------------------------------------------------
# EDIT THIS FILE, then run:  python scripts/gen_neofetch.py
# Everything here is drawn from work you actually do — nothing aspirational.
# -----------------------------------------------------------------------------

USER = "veenus"
HOST = "xeevees-lab"

# Each section: (heading or None, [(key, value), ...])
# Use ("", "") to insert a blank line.
SECTIONS = [
    (None, [
        ("OS",     "Windows 11 + WSL2 (Ubuntu)"),
        ("Shell",  "bash"),
        ("IDE",    "VS Code"),
        ("Host",   "Final-year B.E. AI & DS · SGPI 9.35"),
        ("Kernel", "LLM apps, search & backend · DevOps"),
        ("", ""),
        ("Backend.APIs",     "ASP.NET Core, FastAPI, Fastify, Node.js"),
        ("Backend.Data",     "PostgreSQL, pgvector, Neo4j, ChromaDB"),
        ("Backend.LLM",      "Gemini API, RAG, hybrid retrieval, evals"),
        ("Backend.Testing",  "xUnit, Playwright, Vitest, pytest"),
        ("", ""),
        ("DevOps.Containers", "Docker, Docker Compose"),
        ("DevOps.CI/CD",      "GitLab CI/CD, self-hosted Runner"),
        ("DevOps.Cloud",      "AWS (VPC, EC2, S3, IAM)"),
        ("DevOps.Deploy",     "Render, Vercel, Windows Service"),
        ("DevOps.Security",   "Semgrep, tree-sitter, CWE/OWASP"),
        ("", ""),
        ("Languages.Programming", "Python, C#, TypeScript, JavaScript"),
        ("Languages.Config",      "SQL, YAML, Dockerfile, Bash"),
        ("Languages.Real",        "English, Hindi, Marathi, German (A2)"),
        ("", ""),
        ("Hobbies.Software", "SaaS Products, Automation, Linux Ricing"),
        ("Hobbies.Hardware", "HomeServer, Raspberry Pi, Arduino"),
    ]),
    ("Contact", [
        ("Email",     "veenuspatil0330@gmail.com"),
        ("LinkedIn",  "veenus-patil"),
        ("Instagram", "@xeevee.env"),
        ("GitHub",    "xeevees-lab"),
    ]),
    ("Status", [
        ("Shipped",   "GridLedger · Pramana · AWS VPC lab"),
        ("Currently", "GARDIAN — taint graphs for PR review"),
        ("Open to",   "SDE internships · Pune / Mumbai / Remote"),
        ("Motto",     "If it's not automated, it's not done."),
    ]),
]

# ---- theme: Gruvbox Dark ----------------------------------------------------
BG        = "#1d2021"
FG        = "#ebdbb2"   # values
KEY       = "#fabd2f"   # key labels        (yellow)
ACCENT    = "#fe8019"   # user@host, titles (orange)
BORDER    = "#504945"   # dots, box lines
ART       = "#8ec07c"   # ascii art         (aqua)
GREEN     = "#b8bb26"
RED       = "#fb4934"

PANEL_W   = 66          # width of the right-hand info panel, in characters
FONT_SIZE = 15
LINE_H    = 22
CHAR_W    = 0.6         # advance width of a monospace glyph, in em
PAD       = 26
GAP       = 4           # blank columns between art and info panel

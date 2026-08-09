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
        ("Host",   "Project Lead — GARDIAN (team of 4)"),
        ("Kernel", "Self-hosted DevOps, AI/DS Undergrad"),
        ("", ""),
        ("DevOps.Containers", "Docker, Docker Compose"),
        ("DevOps.CI/CD",      "GitLab CI/CD, self-hosted Runner"),
        ("DevOps.Data",       "Neo4j (Cypher), SQL"),
        ("DevOps.Deploy",     "Render"),
        ("DevOps.Security",   "Semgrep, tree-sitter, CWE/OWASP"),
        ("", ""),
        ("Languages.Programming", "Python, JavaScript, TypeScript, Bash"),
        ("Languages.Config",      "YAML, Dockerfile, SQL, JSON"),
        ("Languages.Real",        "English, Hindi, Marathi, German"),
        ("", ""),
        ("Hobbies.Software", "SaaS Products, Automation, Linux Ricing"),
        ("Hobbies.Hardware", "HomeServer, Raspberry Pi, Arduino"),
    ]),
    ("Contact", [
        ("Email",     "xeeveeslab@gmail.com"),
        ("LinkedIn",  "veenus-patil"),
        ("Instagram", "@xeevee.env"),
        ("GitHub",    "xeevees-lab"),
        ("GitLab",    "gardian1.0/gardian"),
    ]),
    ("Status", [
        ("Currently", "Building GARDIAN — MR security auditor"),
        ("Approach",  "Neo4j taint graphs, self-hosted CI, zero spend"),
        ("Open to",   "Freelance / paid work"),
        ("Motto",     "If it works on my machine, it works on yours."),
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

<div align="center">

<img src="./assets/neofetch.svg" alt="veenus@xeevees-lab" width="100%">

<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-458588?style=for-the-badge&logo=linkedin&logoColor=ebdbb2)](https://linkedin.com/in/veenus-patil)
[![GitLab](https://img.shields.io/badge/GitLab-fe8019?style=for-the-badge&logo=gitlab&logoColor=1d2021)](https://gitlab.com/gardian1.0)
[![Email](https://img.shields.io/badge/Email-cc241d?style=for-the-badge&logo=gmail&logoColor=ebdbb2)](mailto:xeeveeslab@gmail.com)
[![Instagram](https://img.shields.io/badge/Instagram-d3869b?style=for-the-badge&logo=instagram&logoColor=1d2021)](https://instagram.com/xeevee.env)

</div>

---

## Stack

<div align="center">

**Infrastructure & CI/CD**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab%20CI-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-1d2021?style=for-the-badge&logo=linux&logoColor=fabd2f)
![Ubuntu](https://img.shields.io/badge/Ubuntu%20WSL2-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=1d2021)
![Git](https://img.shields.io/badge/Git-F05033?style=for-the-badge&logo=git&logoColor=white)

**Security & Data**

![Semgrep](https://img.shields.io/badge/Semgrep-1B2431?style=for-the-badge&logo=semgrep&logoColor=00C4CC)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=for-the-badge&logo=neo4j&logoColor=white)
![OWASP](https://img.shields.io/badge/OWASP-000000?style=for-the-badge&logo=owasp&logoColor=white)
![tree-sitter](https://img.shields.io/badge/tree--sitter-8ec07c?style=for-the-badge&logo=treesitter&logoColor=1d2021)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langgraph&logoColor=white)

**Languages**

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Bash](https://img.shields.io/badge/Shell-89e051?style=for-the-badge&logo=gnubash&logoColor=1d2021)
![YAML](https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

</div>

---

## GARDIAN

**Graph-Augmented RAG Detection with Intelligent Agent Network** · <!--[gitlab.com/gardian1.0/gardian](https://gitlab.com/gardian1.0/gardian)-->

A self-hosted merge-request security auditor for Python. It flags injection vulnerabilities *before* merge, then posts a patch it has actually executed in a sandbox to prove the fix works.

The point isn't detection — Semgrep already detects. The point is **adjudication**: deciding which findings are real, with grounded evidence, and proving the fix. Semgrep CE runs as the baseline arm in evaluation.

| Stage | How it works |
| :--- | :--- |
| **Candidate generation** | Semgrep CE produces deterministic candidates |
| **Reachability** | Cross-file taint analysis over a Neo4j code property graph, queried in Cypher |
| **Grounding** | RAG over CWE, OWASP and CVEfixes corpora |
| **Adjudication** | Adversarial multi-agent debate via LangGraph |
| **Verification** | Patches executed in a network-isolated Docker sandbox before posting |
| **Delivery** | GitLab CI/CD, self-hosted Runner in Docker |

Built under a hard **zero-cash constraint** — no paid APIs, no cloud GPUs, no managed services. Every component is free-tier or open source, and everything runs locally on WSL2 + Docker. Final-year capstone; I lead a team of four.

<sub>`Python` · `Pydantic v2` · `Semgrep` · `tree-sitter` · `Neo4j` · `Cypher` · `LangGraph` · `sentence-transformers` · `Docker` · `GitLab CI`</sub>

---

## Stats

<div align="center">

<sub>Most of my day-to-day commits live on <a href="https://gitlab.com/gardian1.0">GitLab</a>, so the numbers below only tell part of the story.</sub>

<br><br>

<img height="165" src="https://github-readme-stats.vercel.app/api?username=xeevees-lab&theme=gruvbox&hide_border=true&include_all_commits=true&count_private=true&bg_color=1d2021&title_color=fe8019&icon_color=8ec07c&text_color=ebdbb2">
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=xeevees-lab&theme=gruvbox&hide_border=true&include_all_commits=true&count_private=true&layout=compact&bg_color=1d2021&title_color=fe8019&text_color=ebdbb2">

<img height="165" src="https://streak-stats.demolab.com/?user=xeevees-lab&theme=gruvbox&hide_border=true&background=1d2021">

<img src="https://github-profile-trophy.vercel.app/?username=xeevees-lab&theme=gruvbox&no-frame=true&no-bg=true&column=7&margin-w=6">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/xeevees-lab/xeevees-lab/output/snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/xeevees-lab/xeevees-lab/output/snake.svg">
  <img alt="contribution snake" src="https://raw.githubusercontent.com/xeevees-lab/xeevees-lab/output/snake.svg">
</picture>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=xeevees-lab&theme=gruvbox&hide_border=true&bg_color=1d2021&color=fe8019&line=8ec07c&point=fabd2f&area=true">

</div>

---

<div align="center">

<sub>Open to freelance and paid work &nbsp;·&nbsp; <a href="mailto:xeeveeslab@gmail.com">xeeveeslab@gmail.com</a></sub>

<br>

[![Visitors](https://komarev.com/ghpvc/?username=xeevees-lab&style=for-the-badge&color=fe8019&label=VISITORS)](https://github.com/xeevees-lab)

</div>

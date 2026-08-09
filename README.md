<div align="center">

<img src="./assets/neofetch.svg" alt="veenus@xeevees-lab" width="100%">

<br>

<a href="https://github.com/xeevees-lab">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=21&duration=2600&pause=900&color=FABD2F&center=true&vCenter=true&width=780&height=42&lines=Self-hosted+DevOps%2C+zero+cloud+spend;Security+auditing+that+runs+in+your+own+CI;Neo4j+taint+graphs+%E2%86%92+RAG+%E2%86%92+verified+patches;If+it+works+on+my+machine%2C+it+works+on+yours." alt="what I do">
</a>

<br>

<a href="https://linkedin.com/in/veenus-patil"><img src="https://img.shields.io/badge/LinkedIn-83a598?style=for-the-badge&logo=linkedin&logoColor=1d2021"></a>
<a href="https://gitlab.com/gardian1.0"><img src="https://img.shields.io/badge/GitLab-fe8019?style=for-the-badge&logo=gitlab&logoColor=1d2021"></a>
<a href="mailto:xeeveeslab@gmail.com"><img src="https://img.shields.io/badge/Email-fb4934?style=for-the-badge&logo=gmail&logoColor=fbf1c7"></a>
<a href="https://instagram.com/xeevee.env"><img src="https://img.shields.io/badge/Instagram-d3869b?style=for-the-badge&logo=instagram&logoColor=1d2021"></a>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:504945,50:fabd2f,100:504945&section=header" width="100%">

</div>

<h2 align="center">◆ &nbsp;GARDIAN&nbsp; ◆</h2>

<div align="center">

**G**raph-**A**ugmented **R**AG **D**etection with **I**ntelligent **A**gent **N**etwork

<a href="https://gitlab.com/gardian1.0/gardian"><img src="https://img.shields.io/badge/repo-gitlab.com%2Fgardian1.0-fe8019?style=flat-square&logo=gitlab&logoColor=1d2021"></a>
<img src="https://img.shields.io/badge/status-in%20development-fabd2f?style=flat-square">
<img src="https://img.shields.io/badge/cloud%20spend-%240.00-b8bb26?style=flat-square">
<img src="https://img.shields.io/badge/team-4%20engineers-83a598?style=flat-square">

</div>

<table>
<tr>
<td width="50%" valign="top">

### The problem

Static analysers are loud. Semgrep will happily hand you two hundred findings, most of which aren't reachable, and a reviewer stops reading at forty.

### What GARDIAN does

It doesn't detect harder — it **adjudicates**. Every candidate gets checked for real reachability, grounded against CWE/OWASP evidence, argued over by opposing agents, and if it survives all that, patched with a fix that has already been executed in a sandbox to prove it works.

Semgrep CE runs as the baseline arm, so the improvement is measured, not asserted.

</td>
<td width="50%" valign="top">

### The pipeline

```
  merge request
       │
       ▼
  ① Semgrep CE ........ candidates
       │
       ▼
  ② Neo4j + Cypher .... taint reachable?
       │
       ▼
  ③ RAG ............... CWE · OWASP · CVEfixes
       │
       ▼
  ④ LangGraph ......... agents adjudicate
       │
       ▼
  ⑤ Docker sandbox .... patch verified
       │
       ▼
  GitLab CI posts the fix
```

</td>
</tr>
</table>

<details>
<summary><b>&nbsp;Design constraints, and why they matter&nbsp;</b></summary>

<br>

| Constraint | Consequence |
| :--- | :--- |
| **Zero cash** | No paid APIs, no cloud GPUs, no managed services. Every component is free-tier or open source. |
| **Self-hosted** | Neo4j, the sandbox and the CI runner all live in local Docker on WSL2. Nothing leaves the machine. |
| **One semester** | Aug–Nov 2026, vertical slice first — walking skeleton before breadth. |
| **Air-gappable** | A security tool you can't run on your own infrastructure is a security tool most teams can't adopt. |

The constraints aren't limitations I worked around — they're the reason the thing is adoptable. A PR auditor that ships your source code to a third-party API is a non-starter for exactly the teams that need one most.

<br>

`Python` · `Pydantic v2` · `Semgrep CE` · `tree-sitter` · `Neo4j` · `Cypher` · `LangGraph` · `sentence-transformers` · `Docker` · `GitLab CI`

</details>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:504945,50:8ec07c,100:504945&section=header" width="100%">
</div>

<h2 align="center">◆ &nbsp;Stack&nbsp; ◆</h2>

<table align="center">
<tr>
<td align="right" width="150"><b>Infra&nbsp;&&nbsp;CI</b></td>
<td>
<img src="https://img.shields.io/badge/Docker-83a598?style=flat-square&logo=docker&logoColor=1d2021">
<img src="https://img.shields.io/badge/GitLab_CI-83a598?style=flat-square&logo=gitlab&logoColor=1d2021">
<img src="https://img.shields.io/badge/Linux-83a598?style=flat-square&logo=linux&logoColor=1d2021">
<img src="https://img.shields.io/badge/Ubuntu_WSL2-83a598?style=flat-square&logo=ubuntu&logoColor=1d2021">
<img src="https://img.shields.io/badge/Bash-83a598?style=flat-square&logo=gnubash&logoColor=1d2021">
<img src="https://img.shields.io/badge/Render-83a598?style=flat-square&logo=render&logoColor=1d2021">
<img src="https://img.shields.io/badge/Git-83a598?style=flat-square&logo=git&logoColor=1d2021">
</td>
</tr>
<tr>
<td align="right"><b>Security&nbsp;&&nbsp;Data</b></td>
<td>
<img src="https://img.shields.io/badge/Semgrep-d3869b?style=flat-square&logo=semgrep&logoColor=1d2021">
<img src="https://img.shields.io/badge/Neo4j-d3869b?style=flat-square&logo=neo4j&logoColor=1d2021">
<img src="https://img.shields.io/badge/Cypher-d3869b?style=flat-square&logo=neo4j&logoColor=1d2021">
<img src="https://img.shields.io/badge/OWASP-d3869b?style=flat-square&logo=owasp&logoColor=1d2021">
<img src="https://img.shields.io/badge/tree--sitter-d3869b?style=flat-square&logo=treesitter&logoColor=1d2021">
<img src="https://img.shields.io/badge/LangGraph-d3869b?style=flat-square&logo=langgraph&logoColor=1d2021">
</td>
</tr>
<tr>
<td align="right"><b>Languages</b></td>
<td>
<img src="https://img.shields.io/badge/Python-b8bb26?style=flat-square&logo=python&logoColor=1d2021">
<img src="https://img.shields.io/badge/Shell-b8bb26?style=flat-square&logo=gnubash&logoColor=1d2021">
<img src="https://img.shields.io/badge/YAML-b8bb26?style=flat-square&logo=yaml&logoColor=1d2021">
<img src="https://img.shields.io/badge/TypeScript-b8bb26?style=flat-square&logo=typescript&logoColor=1d2021">
<img src="https://img.shields.io/badge/JavaScript-b8bb26?style=flat-square&logo=javascript&logoColor=1d2021">
<img src="https://img.shields.io/badge/SQL-b8bb26?style=flat-square&logo=mysql&logoColor=1d2021">
</td>
</tr>
</table>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:504945,50:d3869b,100:504945&section=header" width="100%">
</div>

<h2 align="center">◆ &nbsp;Activity&nbsp; ◆</h2>

<div align="center">

<sub><i>Most of my day-to-day commits live on <a href="https://gitlab.com/gardian1.0">GitLab</a> — the numbers below only tell part of the story.</i></sub>

<br><br>

<img height="160" src="https://github-readme-stats.vercel.app/api?username=xeevees-lab&include_all_commits=true&count_private=true&hide_border=true&bg_color=282828&title_color=fabd2f&icon_color=8ec07c&text_color=d5c4a1&ring_color=fe8019">
<img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=xeevees-lab&layout=compact&include_all_commits=true&count_private=true&hide_border=true&bg_color=282828&title_color=fabd2f&text_color=d5c4a1">

<br>

<img height="160" src="https://streak-stats.demolab.com/?user=xeevees-lab&hide_border=true&background=282828&ring=fabd2f&fire=fe8019&currStreakLabel=fabd2f&sideLabels=d5c4a1&dates=928374&stroke=504945&sideNums=d5c4a1&currStreakNum=fbf1c7&dayNums=8ec07c">

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/xeevees-lab/xeevees-lab/output/snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/xeevees-lab/xeevees-lab/output/snake.svg">
  <img alt="contribution snake" src="https://raw.githubusercontent.com/xeevees-lab/xeevees-lab/output/snake.svg">
</picture>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=xeevees-lab&hide_border=true&bg_color=282828&color=fabd2f&line=8ec07c&point=fe8019&title_color=fabd2f&area=true&area_color=8ec07c">

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:504945,50:fe8019,100:504945&section=header" width="100%">

<br>

**"If it works on my machine, it works on yours."**

<a href="mailto:xeeveeslab@gmail.com"><img src="https://img.shields.io/badge/xeeveeslab@gmail.com-fabd2f?style=for-the-badge&logo=gmail&logoColor=1d2021"></a>

<br><br>

<img src="https://komarev.com/ghpvc/?username=xeevees-lab&style=flat-square&color=504945&label=visitors">

</div>

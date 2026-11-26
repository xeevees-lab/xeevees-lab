<div align="center">

<img src="./assets/neofetch.svg" alt="veenus@xeevees-lab" width="100%">

<br>

<a href="https://github.com/xeevees-lab">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=21&duration=2600&pause=900&color=FABD2F&center=true&vCenter=true&width=780&height=42&lines=LLM+apps%2C+search+%26+backend+systems;Hybrid+retrieval+over+pgvector+%2B+Neo4j;Modbus+meters+%E2%86%92+.NET+engine+%E2%86%92+shadow+bills;Taint+graphs+in+my+own+CI;If+it+works+on+my+machine%2C+it+works+on+yours." alt="what I do">
</a>

<sub><b>Final-year B.E. AI &amp; Data Science</b> · SGPI 9.35 &nbsp;|&nbsp; Thane / Mumbai, India &nbsp;|&nbsp; Backend · LLM &amp; search · DevOps</sub>

<a href="https://linkedin.com/in/veenus-patil"><img src="https://img.shields.io/badge/LinkedIn-83a598?style=for-the-badge&logo=linkedin&logoColor=1d2021"></a>
<a href="mailto:veenuspatil0330@gmail.com"><img src="https://img.shields.io/badge/Email-fb4934?style=for-the-badge&logo=gmail&logoColor=fbf1c7"></a>
<a href="https://instagram.com/xeevee.env"><img src="https://img.shields.io/badge/Instagram-d3869b?style=for-the-badge&logo=instagram&logoColor=1d2021"></a>
<img src="https://img.shields.io/badge/Open_to-SDE_Internships-b8bb26?style=for-the-badge&logoColor=1d2021">

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:504945,50:fabd2f,100:504945&section=header" width="100%">

</div>

<h2 align="center">◆ &nbsp;GARDIAN&nbsp; ◆</h2>

<div align="center">

**G**raph-**A**ugmented **R**AG **D**etection with **I**ntelligent **A**gent **N**etwork &nbsp;·&nbsp; <i>final-year major project, team of 4</i>

<i>Reviews pull requests for security holes — and reports only the ones an attacker can actually reach.</i>

<img src="https://img.shields.io/badge/status-in%20development-fabd2f?style=flat-square">
<img src="https://img.shields.io/badge/fixtures-3_TP_·_0_FP-b8bb26?style=flat-square">
<img src="https://img.shields.io/badge/cloud%20spend-%240.00-8ec07c?style=flat-square">
<a href="mailto:veenuspatil0330@gmail.com?subject=GARDIAN%20walkthrough"><img src="https://img.shields.io/badge/source-private_·_walkthrough_on_request-504945?style=flat-square&logo=github&logoColor=fbf1c7"></a>

</div>

<table>
<tr>
<td width="50%" valign="top">

### The problem

Static analysers are loud — hundreds of findings, most unreachable. Reviewers stop reading at forty.

### What GARDIAN does

It doesn't detect harder — it **checks reachability**. Code becomes a Neo4j graph, and a Cypher query traces untrusted input to SQL, shell and `eval` sinks.

Edges carry the **argument position**, so a parameterised query is *not* flagged. Findings are grounded in CWE/OWASP and posted on the PR.

</td>
<td width="50%" valign="top">

### The pipeline

```
 pull request  (PyGithub)
     ▼
 ① tree-sitter .... parse
     ▼
 ② Neo4j CPG ...... data flow
     ▼
 ③ Cypher ......... taint path
     ▼
 ④ RAG ............ CWE · OWASP
     ▼
 PR comment: CWE · flow · fix
     ┊  planned
 ⑤ cross-file taint
 ⑥ LangGraph agents
 ⑦ sandbox-verified patch
```

<sub>①–④ built · unit tests on a self-hosted GitLab Runner · ⑤–⑦ next</sub>

</td>
</tr>
</table>

<details>
<summary><b>&nbsp;Results, decisions & constraints&nbsp;</b></summary>

<br>

**Labelled fixtures** — 4 files, `expected.json` as ground truth:

| Fixture | Expected | GARDIAN | Semgrep CE `p/python` |
| :--- | :---: | :---: | :---: |
| SQLi, direct | CWE-89 | ✅ flagged | ✅ flagged |
| SQLi, 4-hop chain | CWE-89 | ✅ flagged | ⚠️ flagged as CWE-704 |
| Command injection (`os.system`) | CWE-78 | ✅ flagged | ❌ missed |
| Parameterised query | safe | ✅ silent | ✅ silent |

<br>

| Decision | Why |
| :--- | :--- |
| **`HAS_ARG {arg_index}` + per-sink `tainted_args`** | The single reason the parameterised query isn't a false positive. |
| **Taint paths use `*0..N`, not `*1..N`** | `os.system(host)` with no intermediate variable is a zero-hop path. |
| **Recursive node walk, not `queries.scm`** | The py-tree-sitter query API keeps changing shape; a walk survives `pip install -U`. |
| **Semgrep runs as a pinned container** | Its `opentelemetry-sdk` pin breaks the venv — and a containerised baseline is reproducible by anyone. |
| **Zero cash, self-hosted** | Neo4j and the CI runner live in local Docker on WSL2. A security tool you can't run on your own infrastructure is one most teams can't adopt. |

<br>

`Python` · `Pydantic` · `tree-sitter` · `Neo4j` · `Cypher` · `ChromaDB` · `sentence-transformers` · `PyGithub` · `Semgrep CE` · `Docker` · `GitLab CI` · `pytest`

</details>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:504945,50:8ec07c,100:504945&section=header" width="100%">
</div>

<h2 align="center">◆ &nbsp;GridLedger&nbsp; ◆</h2>

<div align="center">

Real-time energy monitoring and electricity-cost control for HT industrial plants.

<i>Shows a factory its electricity bill before the utility does — and how to cut it.</i>

<a href="https://github.com/xeevees-lab/gridledger"><img src="https://img.shields.io/badge/repo-xeevees--lab%2Fgridledger-8ec07c?style=flat-square&logo=github&logoColor=1d2021"></a>
<img src="https://img.shields.io/badge/.NET-10-83a598?style=flat-square&logo=dotnet&logoColor=1d2021">
<img src="https://img.shields.io/badge/PostgreSQL-17-83a598?style=flat-square&logo=postgresql&logoColor=1d2021">
<img src="https://img.shields.io/badge/API_fuzzing-41_→_0_server_errors-b8bb26?style=flat-square">

</div>

<table>
<tr>
<td width="50%" valign="top">

### What it does

A .NET **Windows service** reads energy meters over **Modbus RTU and TCP**, with auto-discovery and a data-quality guard.

It prices every 15 minutes against the published **MSEDCL HT tariff** — demand blocks, kVAh charges, time-of-day rebates — then forecasts load and plans how to shift it off peak.

</td>
<td width="50%" valign="top">

### The engine

```
 energy meters
   │ Modbus RTU / TCP
   ▼
 ① poller ....... DQ guard
   ▼
 ② PostgreSQL ... 15-min blocks
   ▼
 ③ shadow bill .. kVAh · ToD
   ├─► LightGBM forecast
   ├─► OR-Tools load-shift
   ▼
 dashboard + email / Teams
```

</td>
</tr>
</table>

<details>
<summary><b>&nbsp;Controls & testing&nbsp;</b></summary>

<br>

| Area | What's in place |
| :--- | :--- |
| **Audit** | Controls designed to support 21 CFR Part 11 — role-based access, e-signatures, hash-chained audit trail |
| **Security** | Argon2id credentials, dashboard behind a key-secured YARP reverse proxy |
| **Testing** | xUnit + Playwright on simulated meter data; API fuzzing cut server errors from 41 to 0 |
| **Forecasting** | ML.NET LightGBM against a seasonal baseline; Google OR-Tools load-shifting plans |

<br>

`C#` · `.NET 10` · `ASP.NET Core` · `NModbus` · `PostgreSQL 17` · `ML.NET` · `OR-Tools` · `React` · `TypeScript` · `Playwright`

</details>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:504945,50:fe8019,100:504945&section=header" width="100%">
</div>

<h2 align="center">◆ &nbsp;Pramāṇa&nbsp; ◆</h2>

<div align="center">

<b>प्रमाण</b> — <i>"a valid means of knowledge."</i> &nbsp;An LLM news-intelligence platform that separates verified fact from contested claim.

<i>Shows what's verified in the news, what's disputed, and which outlets say what.</i>

<a href="https://github.com/xeevees-lab/pramana"><img src="https://img.shields.io/badge/repo-xeevees--lab%2Fpramana-fabd2f?style=flat-square&logo=github&logoColor=1d2021"></a>
<a href="./assets/pramana-demo.mp4"><img src="https://img.shields.io/badge/demo-watch_video-fe8019?style=flat-square&logo=youtube&logoColor=1d2021"></a>
<img src="https://img.shields.io/badge/tests-91_in_17_suites-b8bb26?style=flat-square">
<img src="https://img.shields.io/badge/REST-27_endpoints-83a598?style=flat-square">
<img src="https://img.shields.io/badge/license-MIT-d3869b?style=flat-square">

<a href="./assets/pramana-demo.mp4"><img src="./assets/pramana-demo.gif" alt="Pramana demo: live dashboard, claim audit and Intelligence search" width="88%"></a>

<sub><i>Live dashboard → claim audit → Intelligence search. &nbsp;Click for the full 2-minute walkthrough.</i></sub>

</div>

<table>
<tr>
<td width="50%" valign="top">

### The problem

Feeds show people news that already agrees with them — the same event, told as two different stories.

### What Pramāṇa does

It ingests RSS, GDELT and NewsAPI every 15 minutes, clusters events, and splits coverage into **atomic claims** — each shown with the outlets that back or dispute it.

Retrieval is measured, not vibes: a 10-category golden benchmark.

</td>
<td width="50%" valign="top">

### The retriever

```
 query
   ▼
 ① intent + thread memory
   ▼
 ② 4 parallel recall lanes
    lexical · pgvector HNSW
    Neo4j graph · event link
   ▼
 ③ weighted rerank → gate
   ▼
 ④ Gemini → answer + ledger
```

<sub>768-d embeddings · 18-table schema mirrored into Neo4j · ~15.5k lines</sub>

</td>
</tr>
</table>

<p align="center">
<code>Gemini API</code> · <code>PostgreSQL</code> · <code>pgvector</code> · <code>Neo4j</code> · <code>Node.js</code> · <code>Fastify</code> · <code>React</code> · <code>Vitest</code> · <code>Render</code> · <code>Vercel</code>
</p>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:504945,50:83a598,100:504945&section=header" width="100%">
</div>

<h2 align="center">◆ &nbsp;Also built&nbsp; ◆</h2>

<table>
<tr>
<td width="33%" valign="top">

#### [AWS VPC Peering Lab](https://github.com/xeevees-lab/aws-vpc-peering-lab)

Two peered VPCs, private EC2s reached through one bastion — then **broke an SG rule on purpose** to prove it controls reachability.

<sub>`AWS VPC` · `EC2` · `Security Groups`</sub>

</td>
<td width="33%" valign="top">

#### [Network Intelligence Dashboard](https://github.com/xeevees-lab/network-intelligence-dashboard)

FastAPI recon tool: **raw-socket port scanner** (100 workers, no nmap), IP geolocation, scan history.

<sub>`Python` · `FastAPI` · `Docker`</sub>

</td>
<td width="33%" valign="top">

#### [Docker-Setup](https://github.com/xeevees-lab/Docker-Setup)

Python 2.7 on Kali, **isolated in a container** instead of breaking the system interpreter.

<sub>`Docker` · `Kali Linux`</sub>

</td>
</tr>
</table>

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
<img src="https://img.shields.io/badge/AWS-83a598?style=flat-square&logo=amazonwebservices&logoColor=1d2021">
<img src="https://img.shields.io/badge/Linux-83a598?style=flat-square&logo=linux&logoColor=1d2021">
<img src="https://img.shields.io/badge/Ubuntu_WSL2-83a598?style=flat-square&logo=ubuntu&logoColor=1d2021">
<img src="https://img.shields.io/badge/Bash-83a598?style=flat-square&logo=gnubash&logoColor=1d2021">
<img src="https://img.shields.io/badge/Render-83a598?style=flat-square&logo=render&logoColor=1d2021">
<img src="https://img.shields.io/badge/Vercel-83a598?style=flat-square&logo=vercel&logoColor=1d2021">
<img src="https://img.shields.io/badge/Git-83a598?style=flat-square&logo=git&logoColor=1d2021">
</td>
</tr>
<tr>
<td align="right"><b>Backend&nbsp;&&nbsp;Data</b></td>
<td>
<img src="https://img.shields.io/badge/ASP.NET_Core-fe8019?style=flat-square&logo=dotnet&logoColor=1d2021">
<img src="https://img.shields.io/badge/FastAPI-fe8019?style=flat-square&logo=fastapi&logoColor=1d2021">
<img src="https://img.shields.io/badge/Node.js-fe8019?style=flat-square&logo=nodedotjs&logoColor=1d2021">
<img src="https://img.shields.io/badge/Fastify-fe8019?style=flat-square&logo=fastify&logoColor=1d2021">
<img src="https://img.shields.io/badge/React-fe8019?style=flat-square&logo=react&logoColor=1d2021">
<img src="https://img.shields.io/badge/PostgreSQL-fe8019?style=flat-square&logo=postgresql&logoColor=1d2021">
<img src="https://img.shields.io/badge/pgvector-fe8019?style=flat-square&logo=postgresql&logoColor=1d2021">
<img src="https://img.shields.io/badge/Neo4j-fe8019?style=flat-square&logo=neo4j&logoColor=1d2021">
<img src="https://img.shields.io/badge/Modbus-fe8019?style=flat-square">
</td>
</tr>
<tr>
<td align="right"><b>LLM&nbsp;&&nbsp;Retrieval</b></td>
<td>
<img src="https://img.shields.io/badge/Gemini_API-fabd2f?style=flat-square&logo=googlegemini&logoColor=1d2021">
<img src="https://img.shields.io/badge/RAG-fabd2f?style=flat-square">
<img src="https://img.shields.io/badge/Hybrid_Retrieval-fabd2f?style=flat-square">
<img src="https://img.shields.io/badge/Reranking-fabd2f?style=flat-square">
<img src="https://img.shields.io/badge/ChromaDB-fabd2f?style=flat-square">
<img src="https://img.shields.io/badge/ML.NET-fabd2f?style=flat-square&logo=dotnet&logoColor=1d2021">
<img src="https://img.shields.io/badge/LLM_Evals-fabd2f?style=flat-square">
</td>
</tr>
<tr>
<td align="right"><b>Security&nbsp;&&nbsp;Testing</b></td>
<td>
<img src="https://img.shields.io/badge/Semgrep-d3869b?style=flat-square&logo=semgrep&logoColor=1d2021">
<img src="https://img.shields.io/badge/tree--sitter-d3869b?style=flat-square&logo=treesitter&logoColor=1d2021">
<img src="https://img.shields.io/badge/Cypher-d3869b?style=flat-square&logo=neo4j&logoColor=1d2021">
<img src="https://img.shields.io/badge/OWASP-d3869b?style=flat-square&logo=owasp&logoColor=1d2021">
<img src="https://img.shields.io/badge/xUnit-d3869b?style=flat-square">
<img src="https://img.shields.io/badge/Playwright-d3869b?style=flat-square&logo=playwright&logoColor=1d2021">
<img src="https://img.shields.io/badge/Vitest-d3869b?style=flat-square&logo=vitest&logoColor=1d2021">
<img src="https://img.shields.io/badge/pytest-d3869b?style=flat-square&logo=pytest&logoColor=1d2021">
</td>
</tr>
<tr>
<td align="right"><b>Languages</b></td>
<td>
<img src="https://img.shields.io/badge/Python-b8bb26?style=flat-square&logo=python&logoColor=1d2021">
<img src="https://img.shields.io/badge/C%23-b8bb26?style=flat-square&logo=dotnet&logoColor=1d2021">
<img src="https://img.shields.io/badge/TypeScript-b8bb26?style=flat-square&logo=typescript&logoColor=1d2021">
<img src="https://img.shields.io/badge/JavaScript-b8bb26?style=flat-square&logo=javascript&logoColor=1d2021">
<img src="https://img.shields.io/badge/SQL-b8bb26?style=flat-square&logo=postgresql&logoColor=1d2021">
<img src="https://img.shields.io/badge/Shell-b8bb26?style=flat-square&logo=gnubash&logoColor=1d2021">
<img src="https://img.shields.io/badge/YAML-b8bb26?style=flat-square&logo=yaml&logoColor=1d2021">
</td>
</tr>
</table>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:504945,50:d3869b,100:504945&section=header" width="100%">
</div>

<h2 align="center">◆ &nbsp;Activity&nbsp; ◆</h2>

<div align="center">

<sub><i>Much of my day-to-day work lives in private repos — the numbers below only tell part of the story.</i></sub>

<br><br>

<img height="150" src="https://github-readme-stats.vercel.app/api/top-langs/?username=xeevees-lab&layout=compact&include_all_commits=true&count_private=true&hide_border=true&bg_color=282828&title_color=fabd2f&text_color=d5c4a1">
<img height="150" src="https://streak-stats.demolab.com/?user=xeevees-lab&hide_border=true&background=282828&ring=fabd2f&fire=fe8019&currStreakLabel=fabd2f&sideLabels=d5c4a1&dates=928374&stroke=504945&sideNums=d5c4a1&currStreakNum=fbf1c7&dayNums=8ec07c">

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/xeevees-lab/xeevees-lab/output/snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/xeevees-lab/xeevees-lab/output/snake.svg">
  <img alt="contribution snake" src="https://raw.githubusercontent.com/xeevees-lab/xeevees-lab/output/snake.svg">
</picture>

<img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=0:504945,50:fe8019,100:504945&section=header" width="100%">

<h3><i>"If it's not automated, it's not done."</i></h3>

<a href="mailto:veenuspatil0330@gmail.com"><img src="https://img.shields.io/badge/Let's_talk-veenuspatil0330@gmail.com-fabd2f?style=for-the-badge&logo=gmail&logoColor=1d2021&labelColor=fe8019"></a>

<br>

<img src="https://komarev.com/ghpvc/?username=xeevees-lab&style=flat-square&color=504945&label=profile+views">

</div>

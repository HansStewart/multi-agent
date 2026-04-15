# Multi-Agent BI System

> A sequential business-intelligence workflow that orchestrates specialized GPT-4o agents to produce a multi-section executive report from one research topic.

**by Hans Stewart &nbsp;·&nbsp; [hansstewart.dev](https://hansstewart.dev)**

[Architecture](https://hansstewart.github.io/ai-architecture) &nbsp;·&nbsp; [Portfolio](https://hansstewart.dev) &nbsp;·&nbsp; [GitHub](https://github.com/HansStewart/multi-agent)

---

## What It Does

Orchestrates specialized GPT-4o agents using CrewAI to produce a multi-section executive report from a single research topic. Each agent stage inherits the full output of the last — building layered, cumulative intelligence rather than isolated one-shot responses.

The result is a coherent, multi-section executive report that reflects the full depth of the pipeline's analysis, not just what a single model pass could produce.

**Design pattern:** sequential specialist agents consistently outperform a single undifferentiated reasoning step.  
**Context model:** each stage inherits the full run context for cumulative intelligence generation.  
**Use cases:** business research, strategic summaries, and high-context executive reporting.

---

## Backend Workflow

**Step 1 — Topic intake** `Input: Research topic`
Receives a research or analysis topic through the API. Builds the run context object used across the entire pipeline. Prepares the sequential execution chain for downstream agents.

**Step 2 — Sequential orchestration** `Intermediate: Cascading context chain`
Uses CrewAI to coordinate sequential multi-agent execution. Each agent stage passes its full output forward as context. Builds layered intelligence rather than isolated one-shot outputs.

**Step 3 — Report assembly** `Processing: Multi-stage synthesis`
Aggregates insights from each specialized agent stage. Formats them into a consistent multi-section report architecture. Ensures continuity and narrative coherence across all sections.

**Step 4 — Final delivery** `Output: Executive intelligence report`
Outputs the completed report through the API in structured form. Supports research synthesis, strategic reviews, and executive briefing workflows. Creates a repeatable intelligence pipeline around one initial prompt.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Framework | Flask |
| Server | Gunicorn |
| Orchestration | CrewAI (sequential pipeline) |
| AI Model | OpenAI GPT-4o |
| Deployment | Google Cloud Run — us-east1 |

---

## Local Development

```bash
git clone https://github.com/HansStewart/multi-agent.git
cd multi-agent
pip install -r requirements.txt
cp .env.example .env
# Add OPENAI_API_KEY to .env
python main.py
```

---

## Environment Variables

| Variable | Required | Purpose |
|---|---|---|
| `OPENAI_API_KEY` | Yes | All agent stages and report generation |

---

## Full Agent Ecosystem

| Agent | Repository |
|---|---|
| Website Audit Agent | [github.com/HansStewart/website-audit-agent](https://github.com/HansStewart/website-audit-agent) |
| AI Content Pipeline | [github.com/HansStewart/ai-content-pipeline](https://github.com/HansStewart/ai-content-pipeline) |
| Voice-to-CRM Agent | [github.com/HansStewart/voice-to-crm](https://github.com/HansStewart/voice-to-crm) |
| Pipeline Intelligence Agent | [github.com/HansStewart/pipeline-intelligence-agent](https://github.com/HansStewart/pipeline-intelligence-agent) |
| CRM Automation Agent | [github.com/HansStewart/crm-agent](https://github.com/HansStewart/crm-agent) |
| AI Data Agent | [github.com/HansStewart/ai-data-agent](https://github.com/HansStewart/ai-data-agent) |
| RAG Document Intelligence | [github.com/HansStewart/rag-agent](https://github.com/HansStewart/rag-agent) |
| AI Architecture | [hansstewart.github.io/ai-architecture](https://hansstewart.github.io/ai-architecture) |

---

**Hans Stewart &nbsp;·&nbsp; Marketing Automation Engineer &nbsp;·&nbsp; [hansstewart.dev](https://hansstewart.dev)**

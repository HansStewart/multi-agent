# 🧠 Multi-Agent BI System

     

A multi-agent business intelligence system that orchestrates 4 specialized GPT-4o agents in a sequential CrewAI pipeline. Each agent passes its complete output as context to the next, producing a 6-section executive intelligence report on any research topic.

**Live API:** `https://multi-agent-559169459241.us-east1.run.app`

***

## Architecture

```
POST /analyze  { "topic": "..." }
        │
        ▼
┌───────────────────────────────────────────────────────────┐
│                  CrewAI Sequential Pipeline               │
│                  Process.sequential · verbose=True        │
│                                                           │
│  ┌──────────────┐    ┌──────────────┐                     │
│  │   Agent 01   │───▶│   Agent 02   │                     │
│  │   Research   │    │   BI Analyst │                     │
│  │   Analyst    │    │              │                     │
│  └──────────────┘    └──────┬───────┘                     │
│                             │ context                     │
│                             ▼                             │
│                    ┌──────────────┐    ┌──────────────┐   │
│                    │   Agent 03   │───▶│   Agent 04   │   │
│                    │   Report     │    │   QA         │   │
│                    │   Writer     │    │   Specialist │   │
│                    └──────────────┘    └──────────────┘   │
└───────────────────────────────────────────────────────────┘
        │
        ▼
  6-Section Executive Report + execution_time + agents_used
```

***

## Tech Stack

| Layer | Technology |
|---|---|
| Runtime | Python 3.11 |
| Agent Orchestration | CrewAI 0.80 |
| Web Framework | Flask 3.0 + Gunicorn |
| AI / LLM | OpenAI GPT-4o (all agents) |
| Process Type | Sequential (context chaining) |
| Containerization | Docker (python:3.11-slim) |
| Cloud | Google Cloud Run — us-east1 |

***

## The Pipeline — 4 Agents, 4 Tasks

### Agent 01 — Senior Research Analyst
**Role:** Gathers comprehensive background on the topic  
**Output:**
- Key facts and current state of the topic
- Major trends (2024–2026)
- Key stakeholders and market players
- Challenges and opportunities
- Relevant statistics and data points

### Agent 02 — BI Analyst
**Role:** Receives Agent 01's full output as context, performs deep analysis  
**Output:**
- 3–5 key insights extracted from the research
- Pattern and trend recognition
- Risk assessment
- Business implications
- Data-driven conclusions

### Agent 03 — Report Writer
**Role:** Receives Agents 01+02 context, writes the structured report  
**Output:**
- Executive Summary
- Market Overview
- Key Findings
- Strategic Analysis
- Recommendations

### Agent 04 — QA Specialist
**Role:** Receives full context from all prior agents, reviews and finalizes  
**Output:**
- Accuracy review
- Logical flow check
- Clarity and readability polish
- Completeness audit
- Final approved report

***

## API Reference

### `GET /`
Health check + agent manifest.

**Response:**
```json
{
  "status": "healthy",
  "service": "Multi-Agent BI System",
  "agents": ["Research Analyst", "BI Analyst", "Report Writer", "QA Specialist"],
  "endpoints": ["/analyze", "/quick-analyze"]
}
```

***

### `POST /analyze`
Full 4-agent pipeline. Estimated time: ~4 minutes.

**Request:**
```json
{ "topic": "AI adoption in commercial real estate 2026" }
```

**Response:**
```json
{
  "topic": "AI adoption in commercial real estate 2026",
  "report": {
    "executive_summary": "...",
    "market_overview": "...",
    "key_findings": "...",
    "strategic_analysis": "...",
    "recommendations": "...",
    "conclusion": "..."
  },
  "agents_used": ["Research Analyst", "BI Analyst", "Report Writer", "QA Specialist"],
  "tasks_completed": 4,
  "execution_time_seconds": 241
}
```

***

### `POST /quick-analyze`
Fast 2-agent pipeline (Research Analyst + Report Writer). Estimated time: ~2 minutes.

**Request:**
```json
{ "topic": "fitness studio lead generation trends" }
```

**Response:**
```json
{
  "topic": "fitness studio lead generation trends",
  "report": { "summary": "...", "findings": "...", "recommendations": "..." },
  "agents_used": ["Research Analyst", "Report Writer"],
  "tasks_completed": 2,
  "execution_time_seconds": 118
}
```

***

## How It Works

CrewAI's `Process.sequential` runs each agent task in order, automatically passing the full output of every prior agent as context to the next. This means:

- Agent 02 sees everything Agent 01 produced
- Agent 03 sees everything Agents 01 and 02 produced
- Agent 04 sees the complete chain — research, analysis, and draft report — before making final edits

Each agent has `max_iter=3`, meaning it can self-correct up to 3 times before returning its output.

***

## Local Setup

```bash
git clone https://github.com/HansStewart/multi-agent.git
cd multi-agent
pip install -r requirements.txt
```

Create a `.env` file:
```
OPENAI_API_KEY=your_key_here
```

Run the server:
```bash
python main.py
```

Test the pipeline:
```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"topic": "AI in marketing automation"}'
```

***

## Project Structure

```
multi-agent/
├── app/
│   ├── agents.py         # 4 CrewAI agent definitions
│   ├── tasks.py          # 4 task definitions with context chaining
│   ├── crew.py           # CrewAI Crew + Process.sequential config
│   └── routes.py         # Flask endpoints
├── main.py               # App entry point
├── Dockerfile
├── requirements.txt
└── README.md
```

***

## Deployment

```bash
gcloud run deploy multi-agent \
  --source . \
  --platform managed \
  --region us-east1 \
  --allow-unauthenticated \
  --set-env-vars OPENAI_API_KEY=...
```

***

## Architecture Diagram

Full system architecture across all 4 agents:  
🔗 [hansstewart.github.io/ai-architecture](https://hansstewart.github.io/ai-architecture)

***

## Part of the AI Agent Portfolio

| Agent | Description | Live URL |
|---|---|---|
| AI Data Agent | CSV analysis + GPT-4o insights | [↗](https://ai-data-agent-559169459241.us-east1.run.app) |
| RAG Document Intelligence | FAISS vector search + cited Q&A | [↗](https://rag-agent-559169459241.us-east1.run.app) |
| CRM Automation Agent | HubSpot + lead scoring + email gen | [↗](https://crm-agent-559169459241.us-east1.run.app) |
| **Multi-Agent BI System** | CrewAI 4-agent pipeline | [↗](https://multi-agent-559169459241.us-east1.run.app) |

**Author:** [Hans Stewart](https://github.com/HansStewart)
Multi-Agent Business Intelligence System
A production-ready multi-agent AI system that orchestrates 4 specialized GPT-4o agents in a sequential pipeline to deliver professional-grade business intelligence reports on any topic — deployed live on Google Cloud Run.

| [rag-agent](https://github.com/HansStewart/rag-agent) | Document Q&A with FAISS vector search | [Live](https://rag-agent-559169459241.us-east1.run.app) |

🔗 Live API: https://multi-agent-559169459241.us-east1.run.app

The Problem It Solves
Traditional research is slow, shallow, and unstructured. Hiring a research analyst for a single report is expensive. Generic AI responses lack structure, citations, and business relevance.

This system solves all three — 4 AI agents collaborate in sequence, each doing one job with expert precision, delivering a fully structured, executive-ready business intelligence report in minutes.

Agent Architecture
text
┌─────────────────────────────────────────────────────────────────┐
│                  MULTI-AGENT PIPELINE (Sequential)              │
│                                                                 │
│  📥 Topic Input                                                 │
│       │                                                         │
│       ▼                                                         │
│  ┌─────────────────────┐                                        │
│  │  Agent 1            │                                        │
│  │  Senior Research    │  → Gathers facts, trends, data,       │
│  │  Analyst            │    stakeholders & recent developments  │
│  └──────────┬──────────┘                                        │
│             │                                                   │
│             ▼                                                   │
│  ┌─────────────────────┐                                        │
│  │  Agent 2            │                                        │
│  │  Business           │  → Extracts insights, patterns,       │
│  │  Intelligence       │    risks, opportunities & implications │
│  │  Analyst            │                                        │
│  └──────────┬──────────┘                                        │
│             │                                                   │
│             ▼                                                   │
│  ┌─────────────────────┐                                        │
│  │  Agent 3            │                                        │
│  │  Senior Business    │  → Writes structured 6-section        │
│  │  Report Writer      │    executive business report           │
│  └──────────┬──────────┘                                        │
│             │                                                   │
│             ▼                                                   │
│  ┌─────────────────────┐                                        │
│  │  Agent 4            │                                        │
│  │  Quality Assurance  │  → Reviews, refines & polishes        │
│  │  Specialist         │    for executive presentation          │
│  └──────────┬──────────┘                                        │
│             │                                                   │
│             ▼                                                   │
│  📤 Structured Business Intelligence Report                     │
└─────────────────────────────────────────────────────────────────┘
Report Output Structure
Every full analysis produces a professionally structured 6-section report:

Executive Summary — High-level synthesis for decision makers

Market Overview — Current state of the landscape

Key Findings — The most important discoveries

Strategic Analysis — Patterns, risks, and opportunities

Recommendations — 3–5 specific, actionable next steps

Conclusion — Synthesis and forward-looking insight

API Endpoints
GET /
Health check — confirms the system is live and lists all agents and endpoints.

Response:

json
{
  "message": "Multi-Agent Business Intelligence System",
  "status": "healthy",
  "powered_by": "CrewAI + OpenAI GPT-4o",
  "agents": [
    "Senior Research Analyst",
    "Business Intelligence Analyst",
    "Senior Business Report Writer",
    "Quality Assurance Specialist"
  ]
}
POST /analyze
Full 4-agent sequential pipeline. Delivers the highest-quality, fully reviewed business intelligence report.

Request:

json
{
  "topic": "AI trends in healthcare 2026"
}
Response:

json
{
  "status": "success",
  "topic": "AI trends in healthcare 2026",
  "report": "## Executive Summary\n...",
  "agents_used": ["Senior Research Analyst", "Business Intelligence Analyst", "Senior Business Report Writer", "Quality Assurance Specialist"],
  "tasks_completed": 4,
  "process": "Sequential Multi-Agent Pipeline",
  "execution_time_seconds": 187.4
}
⏱️ Typical execution time: 3–5 minutes

POST /quick-analyze
2-agent fast pipeline. Research + Writing only, no analysis or QA pass. Best for rapid overviews.

Request:

json
{
  "topic": "Real estate market trends 2026"
}
Response:

json
{
  "status": "success",
  "topic": "Real estate market trends 2026",
  "report": "## Executive Summary\n...",
  "agents_used": ["Senior Research Analyst", "Senior Business Report Writer"],
  "tasks_completed": 2,
  "process": "Quick 2-Agent Pipeline",
  "execution_time_seconds": 94.2
}
⏱️ Typical execution time: 1–3 minutes

Tech Stack
Layer	Technology
Agent Framework	CrewAI 0.80.0
LLM	OpenAI GPT-4o
API Server	Flask 3.0.3
CORS	Flask-CORS
Containerization	Docker (python:3.11-slim)
Cloud Deployment	Google Cloud Run (us-east1)
Production Server	Gunicorn
Language	Python 3.11
Project Structure
text
multi-agent/
├── app/
│   ├── __init__.py         # Flask app factory
│   ├── agents.py           # 4 specialized CrewAI agent definitions
│   ├── tasks.py            # Task definitions with context chaining
│   ├── crew_runner.py      # Crew orchestration (full & quick pipelines)
│   └── routes.py           # REST API endpoints
├── main.py                 # Application entry point
├── Dockerfile              # Container configuration
├── requirements.txt        # Pinned dependencies
├── test_agents.py          # API test suite
└── .env                    # Environment variables (not committed)
Local Setup
Prerequisites
Python 3.11

OpenAI API Key

Installation
bash
# Clone the repository
git clone https://github.com/HansStewart/multi-agent.git
cd multi-agent

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Add your OPENAI_API_KEY to .env
Run Locally
bash
python main.py
API will be available at http://localhost:8080

Test
bash
python test_agents.py
Example Use Cases
Market Research — "Competitive landscape of CRM software for small businesses 2026"

Industry Analysis — "AI adoption trends in real estate 2026"

Strategic Intelligence — "Opportunities in fitness technology for boutique studios"

Technology Briefings — "State of multi-agent AI frameworks for enterprise use"

Investment Research — "Emerging markets in health tech post-2025"

Deployment
Deployed on Google Cloud Run using Docker containerization. The service auto-scales to handle concurrent requests with a 300-second timeout to accommodate multi-agent processing time.

bash
gcloud run deploy multi-agent \
  --source . \
  --platform managed \
  --region us-east1 \
  --allow-unauthenticated \
  --timeout=300 \
  --set-env-vars OPENAI_API_KEY=your_key \
  --memory 2Gi

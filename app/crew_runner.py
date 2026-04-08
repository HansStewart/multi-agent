from crewai import Crew, Process
from app.agents import (
    create_research_agent,
    create_analysis_agent,
    create_writer_agent,
    create_reviewer_agent
)
from app.tasks import (
    create_research_task,
    create_analysis_task,
    create_writing_task,
    create_review_task
)
import time

def run_business_intelligence_crew(topic):
    start_time = time.time()

    research_agent = create_research_agent()
    analysis_agent = create_analysis_agent()
    writer_agent = create_writer_agent()
    reviewer_agent = create_reviewer_agent()

    research_task = create_research_task(research_agent, topic)
    analysis_task = create_analysis_task(analysis_agent, topic, research_task)
    writing_task = create_writing_task(writer_agent, topic, analysis_task)
    review_task = create_review_task(reviewer_agent, topic, writing_task)

    crew = Crew(
        agents=[research_agent, analysis_agent, writer_agent, reviewer_agent],
        tasks=[research_task, analysis_task, writing_task, review_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    end_time = time.time()

    return {
        "topic": topic,
        "report": str(result),
        "agents_used": [
            "Senior Research Analyst",
            "Business Intelligence Analyst",
            "Senior Business Report Writer",
            "Quality Assurance Specialist"
        ],
        "tasks_completed": 4,
        "process": "Sequential Multi-Agent Pipeline",
        "execution_time_seconds": round(end_time - start_time, 2)
    }

def run_quick_analysis(topic):
    start_time = time.time()

    research_agent = create_research_agent()
    writer_agent = create_writer_agent()

    research_task = create_research_task(research_agent, topic)
    writing_task = create_writing_task(writer_agent, topic, research_task)

    crew = Crew(
        agents=[research_agent, writer_agent],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    end_time = time.time()

    return {
        "topic": topic,
        "report": str(result),
        "agents_used": [
            "Senior Research Analyst",
            "Senior Business Report Writer"
        ],
        "tasks_completed": 2,
        "process": "Quick 2-Agent Pipeline",
        "execution_time_seconds": round(end_time - start_time, 2)
    }
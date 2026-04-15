from crewai import Crew, Process, LLM
from app.agents import create_research_agent, create_analysis_agent, create_writer_agent
from app.tasks import create_research_task, create_analysis_task, create_writing_task
import time

def run_business_intelligence_crew(topic):
    start_time = time.time()

    research_agent = create_research_agent()
    research_agent.llm = LLM(model="gpt-4o-mini")

    analysis_agent = create_analysis_agent()
    analysis_agent.llm = LLM(model="gpt-4o-mini")

    writer_agent = create_writer_agent()

    research_task = create_research_task(research_agent, topic)
    analysis_task = create_analysis_task(analysis_agent, topic, research_task)
    writing_task = create_writing_task(writer_agent, topic, analysis_task)

    crew = Crew(
        agents=[research_agent, analysis_agent, writer_agent],
        tasks=[research_task, analysis_task, writing_task],
        process=Process.sequential,
        verbose=False
    )

    result = crew.kickoff()
    end_time = time.time()

    report_text = str(result)

    sections = {}
    for section in ["EXECUTIVE SUMMARY", "KEY FINDINGS", "STRATEGIC ANALYSIS", "RECOMMENDATIONS", "CONCLUSION"]:
        start = report_text.find(section)
        if start != -1:
            next_sections = [s for s in ["EXECUTIVE SUMMARY", "KEY FINDINGS", "STRATEGIC ANALYSIS", "RECOMMENDATIONS", "CONCLUSION"] if s != section]
            end = len(report_text)
            for ns in next_sections:
                pos = report_text.find(ns, start + len(section))
                if pos != -1 and pos < end:
                    end = pos
            sections[section.lower().replace(" ", "_")] = report_text[start + len(section):end].strip()

    return {
        "topic": topic,
        "report": sections if sections else {"full_report": report_text},
        "agents_used": ["Research Analyst", "BI Analyst", "Report Writer"],
        "tasks_completed": 3,
        "process": "3-Agent Sequential Pipeline",
        "execution_time_seconds": round(end_time - start_time, 2)
    }

def run_quick_analysis(topic):
    start_time = time.time()

    research_agent = create_research_agent()
    research_agent.llm = LLM(model="gpt-4o-mini")

    writer_agent = create_writer_agent()

    research_task = create_research_task(research_agent, topic)
    writing_task = create_writing_task(writer_agent, topic, research_task)

    crew = Crew(
        agents=[research_agent, writer_agent],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=False
    )

    result = crew.kickoff()
    end_time = time.time()

    return {
        "topic": topic,
        "report": {"full_report": str(result)},
        "agents_used": ["Research Analyst", "Report Writer"],
        "tasks_completed": 2,
        "process": "Quick 2-Agent Pipeline",
        "execution_time_seconds": round(end_time - start_time, 2)
    }
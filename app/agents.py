from crewai import Agent
from dotenv import load_dotenv
import os

load_dotenv()

def create_research_agent():
    return Agent(
        role="Senior Research Analyst",
        goal="Research and summarize the most important facts and trends on the given topic",
        backstory="""You are a sharp research analyst who delivers concise, 
        high-signal findings. You skip filler and focus on what matters most.""",
        verbose=False,
        allow_delegation=False,
        max_iter=1
    )

def create_analysis_agent():
    return Agent(
        role="Business Intelligence Analyst",
        goal="Extract the top 3-5 actionable insights from the research",
        backstory="""You are a focused BI analyst who identifies the most 
        important patterns and business implications quickly and precisely.""",
        verbose=False,
        allow_delegation=False,
        max_iter=1
    )

def create_writer_agent():
    return Agent(
        role="Senior Business Report Writer",
        goal="Write a sharp, professional executive intelligence report",
        backstory="""You write concise, executive-ready business reports. 
        You make complex information clear and every section earns its place.""",
        verbose=False,
        allow_delegation=False,
        max_iter=1
    )
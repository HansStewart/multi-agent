from crewai import Task

def create_research_task(agent, topic):
    return Task(
        description=f"""Research this topic: {topic}

        Deliver ONLY:
        - 3-5 key facts and current state
        - 2-3 major trends (2024-2026)
        - Top challenges and opportunities
        - Key statistics if available

        Be concise. No filler. Maximum 300 words.""",
        agent=agent,
        expected_output="Concise research summary under 300 words covering key facts, trends, and opportunities."
    )

def create_analysis_task(agent, topic, research_task):
    return Task(
        description=f"""Analyze research findings about: {topic}

        Deliver ONLY:
        - Top 3 insights from the research
        - 1-2 key risks
        - 1-2 key opportunities
        - Core business implication in 1-2 sentences

        Be direct. Maximum 200 words.""",
        agent=agent,
        expected_output="Strategic analysis under 200 words with top insights, risks, and opportunities.",
        context=[research_task]
    )

def create_writing_task(agent, topic, analysis_task):
    return Task(
        description=f"""Write a complete business intelligence report on: {topic}

        Use the research and analysis provided. Structure it exactly as:

        EXECUTIVE SUMMARY
        [2 paragraphs max]

        KEY FINDINGS
        [3-4 bullet points]

        STRATEGIC ANALYSIS
        [2-3 paragraphs]

        RECOMMENDATIONS
        [3 specific, actionable items]

        CONCLUSION
        [1 paragraph]

        Professional tone. No fluff. Accuracy and clarity over length.""",
        agent=agent,
        expected_output="Complete 5-section business intelligence report, professional and concise.",
        context=[analysis_task]
    )
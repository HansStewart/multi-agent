from crewai import Task

def create_research_task(agent, topic):
    return Task(
        description=f"""Research the following topic thoroughly:

        Topic: {topic}

        Your research should include:
        1. Key facts and current state of the topic
        2. Major trends and developments
        3. Key players, companies, or stakeholders involved
        4. Challenges and opportunities
        5. Recent developments (2024-2026)
        6. Statistical data and metrics where available

        Provide comprehensive, well-organized research findings.""",
        agent=agent,
        expected_output="""A comprehensive research report with:
        - Key facts and overview
        - Current trends and developments
        - Major stakeholders and players
        - Challenges and opportunities
        - Supporting data and statistics"""
    )

def create_analysis_task(agent, topic, research_task):
    return Task(
        description=f"""Analyze the research findings about: {topic}

        Based on the research provided, perform a deep analysis:
        1. Identify the 3-5 most significant insights
        2. Analyze patterns and trends
        3. Assess opportunities and risks
        4. Compare different perspectives or approaches
        5. Draw data-driven conclusions
        6. Identify what this means for businesses or decision makers""",
        agent=agent,
        expected_output="""A strategic analysis including:
        - Top 3-5 key insights
        - Pattern and trend analysis
        - Opportunity and risk assessment
        - Strategic conclusions
        - Business implications""",
        context=[research_task]
    )

def create_writing_task(agent, topic, analysis_task):
    return Task(
        description=f"""Write a professional business intelligence report on: {topic}

        Using the research and analysis provided, create a comprehensive report with:

        1. EXECUTIVE SUMMARY (2-3 paragraphs)
        2. MARKET OVERVIEW
        3. KEY FINDINGS
        4. STRATEGIC ANALYSIS
        5. RECOMMENDATIONS (3-5 specific, actionable)
        6. CONCLUSION

        Write in a professional, clear style suitable for executives.""",
        agent=agent,
        expected_output="""A complete professional business report with all 6 sections:
        Executive Summary, Market Overview, Key Findings,
        Strategic Analysis, Recommendations, and Conclusion""",
        context=[analysis_task]
    )

def create_review_task(agent, topic, writing_task):
    return Task(
        description=f"""Review and improve the business report on: {topic}

        Review the report for:
        1. Accuracy and factual correctness
        2. Logical flow and structure
        3. Clarity and readability
        4. Completeness of all sections
        5. Professional tone and language
        6. Actionability of recommendations
        7. Overall impact and value

        Provide the final polished version ready for executive presentation.""",
        agent=agent,
        expected_output="""The final polished, executive-ready business intelligence
        report with all improvements incorporated. Must include all 6 sections.""",
        context=[writing_task]
    )
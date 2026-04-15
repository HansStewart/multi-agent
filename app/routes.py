from flask import Blueprint, request, jsonify
from app.crew_runner import run_business_intelligence_crew, run_quick_analysis

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Multi-Agent Business Intelligence System",
        "status": "healthy",
        "powered_by": "CrewAI + OpenAI GPT-4o",
        "agents": [
    "Research Analyst",
    "Business Intelligence Analyst",
    "Report Writer"
],
        "endpoints": {
            "POST /analyze": "Full 4-agent business intelligence report",
            "POST /quick-analyze": "Fast 2-agent quick analysis"
        }
    })

@main.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'topic' not in data:
        return jsonify({
            "error": "Please provide a topic",
            "example": {"topic": "AI trends in healthcare 2026"}
        }), 400
    topic = data['topic']
    try:
        print(f"\n🚀 Starting 4-agent crew for topic: {topic}")
        result = run_business_intelligence_crew(topic)
        return jsonify({"status": "success", **result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    if not data or 'topic' not in data:
        return jsonify({"error": "Please provide a topic"}), 400
    topic = data['topic']
    try:
        print(f"\n🎯 Portfolio query: {topic}")
        result = run_business_intelligence_crew(topic)
        return jsonify({"status": "success", **result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
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
            "Senior Research Analyst",
            "Business Intelligence Analyst",
            "Senior Business Report Writer",
            "Quality Assurance Specialist"
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

@main.route('/quick-analyze', methods=['POST'])
def quick_analyze():
    data = request.get_json()
    if not data or 'topic' not in data:
        return jsonify({
            "error": "Please provide a topic",
            "example": {"topic": "Real estate market trends 2026"}
        }), 400
    topic = data['topic']
    try:
        print(f"\n⚡ Starting 2-agent quick analysis for: {topic}")
        result = run_quick_analysis(topic)
        return jsonify({"status": "success", **result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
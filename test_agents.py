import requests
import json

BASE_URL = "http://localhost:8080"

print("🚀 Testing Multi-Agent Business Intelligence System\n")
print("=" * 60)

print("\n✅ Test 1: Health Check")
r = requests.get(f"{BASE_URL}/")
data = r.json()
print(f"Status: {data['status']}")
print(f"Powered by: {data['powered_by']}")
print(f"Agents: {', '.join(data['agents'])}")

print("\n✅ Test 2: Quick Analysis (2 Agents)")
print("Topic: AI trends in real estate 2026")
print("Running... (this takes 1-2 minutes)")
r = requests.post(
    f"{BASE_URL}/quick-analyze",
    json={"topic": "AI trends in real estate industry 2026"},
    timeout=300
)
result = r.json()
print(f"Status: {result['status']}")
print(f"Agents used: {result['agents_used']}")
print(f"Tasks completed: {result['tasks_completed']}")
print(f"Execution time: {result['execution_time_seconds']} seconds")
print(f"\nReport Preview:\n{result['report'][:500]}...")

print("\n" + "=" * 60)
print("🎉 Tests complete!")
print("=" * 60)
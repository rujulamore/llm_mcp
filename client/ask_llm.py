import requests
import re



def ask_mcp(query):
    if "weather" in query:
        city = query.split("in")[-1].strip()
        city = re.sub(r'[^a-zA-Z ]', '', city).strip().lower()
        return requests.get("http://localhost:8000/weather", params={"city": city}).json()
    elif "github" in query:
        repo = query.split("for")[-1].strip()
        return requests.get("http://localhost:8000/github", params={"repo": repo}).json()
    else:
        return {"error": "Service not supported"}

# Simulate LLM question
query = input("Ask something: ")
response = ask_mcp(query)
print("🔍 Response:", response)

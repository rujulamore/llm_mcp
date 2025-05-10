from fastapi import FastAPI
from plugins.weather import get_weather
from plugins.github import get_repo_stats

app = FastAPI()

@app.get("/weather")
def weather(city: str):
    return get_weather(city)

@app.get("/github")
def github(repo: str):
    return get_repo_stats(repo)

def get_repo_stats(repo):
    fake_stats = {
        "anthropic/mcp": {"stars": 4200, "forks": 300},
        "openai/gpt": {"stars": 65000, "forks": 5200},
    }
    return fake_stats.get(repo.lower(), {"error": "Repo not found"})

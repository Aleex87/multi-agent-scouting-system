from agents.planner import PlannerAgent

team = {
    "name": "My Team",
    "players": [
        {"name": "Player1", "role": "Forward", "score": 90},
        {"name": "Player2", "role": "Midfielder", "score": 60},
        {"name": "Player3", "role": "Defender", "score": 70},
    ]
}

planner = PlannerAgent()
result = planner.run(team)

print(result)
from agents.planner import PlannerAgent
from agents.doer import DoerAgent
from agents.critic import CriticAgent

team = {
    "name": "My Team",
    "players": [
        {"name": "Player1", "role": "Forward", "score": 90},
        {"name": "Player2", "role": "Midfielder", "score": 60},
        {"name": "Player3", "role": "Defender", "score": 70},
    ]
}

planner = PlannerAgent()
doer = DoerAgent()
critic = CriticAgent()

plan = planner.run(team)
candidate = doer.run(plan)
review = critic.run(candidate)

print(review)
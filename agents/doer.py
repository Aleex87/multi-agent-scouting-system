from utils.logger import log
import random

class DoerAgent:
    def run(self, plan: dict) -> dict:
        log("Doer: searching for candidate player")

        target_role = plan["target_role"]

        # fake market with players
        fake_market = [
            {"name": "Player A", "role": "Midfielder", "value": 80},
            {"name": "Player B", "role": "Midfielder", "value": 75},
            {"name": "Player C", "role": "Defender", "value": 85},
            {"name": "Player D", "role": "Forward", "value": 90},
            {"name": "Player E", "role": "Midfielder", "value": 82},
        ]

        # filter by role 
        candidates = [p for p in fake_market if p["role"] == target_role]

        if not candidates:
            log("Doer: no candidates found for role")
            return None

        candidate = random.choice(candidates)

        result = {
            "candidate": candidate,
            "reason": "Selected based on role match and simulated evaluation"
        }

        log(f"Doer result: {result}")
        return result
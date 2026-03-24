from utils.logger import log

class PlannerAgent:
    def run(self, team: dict) -> dict:
        log("Planner: analyzing team")

        weakest_player = min(team["players"], key=lambda player: player["score"])

        result = {
            "target_role": weakest_player["role"],
            "player_to_replace": weakest_player["name"],
            "reason": "Lowest performance score in the team"
        }

        log(f"Planner result: {result}")
        return result
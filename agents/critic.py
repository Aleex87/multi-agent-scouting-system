from utils.logger import log

class CriticAgent:
    def run(self, candidate_data: dict) -> dict:
        log("Critic: evaluating candidate")

        if candidate_data is None:
            log("Critic: no candidate received")
            return {
                "approved": False,
                "candidate": None,
                "reason": "No candidate provided"
            }
        # Handoff 
        candidate = candidate_data["candidate"]

        # Semple role 
        is_valid = candidate["value"] > 75

        if is_valid:
            reason = "Candidate meets value threshold"
        else:
            reason = "Candidate value too low"

        result = {
            "approved": is_valid,
            "candidate": candidate,
            "reason": reason
        }

        log(f"Critic result: {result}")
        return result
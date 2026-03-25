from agents.planner import PlannerAgent
from agents.doer import DoerAgent
from agents.critic import CriticAgent
from utils.logger import log

class Workflow:
    def __init__(self):
        self.planner = PlannerAgent()
        self.doer = DoerAgent()
        self.critic = CriticAgent()

    def run(self, team: dict):
        log("Workflow started")

        # max_iterations based on the number of players in a teem
        max_iterations = len(team["players"])
        log(f"Max iterations set to {max_iterations}")

        # STEP 1: Planner
        plan = self.planner.run(team)

        # STEP 2: Loop
        for i in range(max_iterations):
            log(f"Iteration {i+1}/{max_iterations}")

            candidate = self.doer.run(plan)
            review = self.critic.run(candidate)

            # if there is not a valid candidate
            if review["approved"]:
                log("Workflow: candidate approved, stopping loop")
                return {
                   "plan": plan,
                    "candidate": review["candidate"]
                        }

        log("Workflow: no valid candidate found after max iterations")
        return None
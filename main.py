from orchestrator.workflow import Workflow
from utils.logger import log


def human_decision(plan, candidate):
    print("\n--- SCOUTING REPORT ---")
    print(f"Player to replace: {plan['player_to_replace']}")
    print(f"Target role: {plan['target_role']}")

    print("\nSuggested replacement:")
    print(candidate)

    decision = input("\nDo you accept this player? (y/n): ")
    return decision.lower() == "y"


if __name__ == "__main__":
    team = {
        "name": "My Team",
        "players": [
            {"name": "Player1", "role": "Forward", "score": 90},
            {"name": "Player2", "role": "Midfielder", "score": 60},
            {"name": "Player3", "role": "Defender", "score": 70},
        ]
    }

    workflow = Workflow()
    result = workflow.run(team)

    if result:
        approved = human_decision(
            plan=result["plan"],
            candidate=result["candidate"]
        )

        if approved:
            log("Human accepted the suggestion")
            print("\nAction: You can now proceed with the transfer.")
        else:
            log("Human rejected the suggestion")
            print("\nAction: No changes applied. You may run the workflow again.")
    else:
        log("No valid candidate found")
from utils.models import get_model
import json
import re
from orchestrator.workflow import Workflow
from utils.logger import log


def human_decision(plan, candidate):
    print("\n--- SCOUTING REPORT ---")
    print(f"Player to replace: {plan['player_to_replace']}")
    print(f"Target role: {plan['target_role']}")

    print("\nSuggested replacement:")
    print(f"Name: {candidate['name']}")
    print(f"Role: {candidate['role']}")
    print(f"Value: {candidate['value']}")
    decision = input("\nDo you accept this player? (y/n): ")
    return decision.lower() == "y"


def generate_team_from_llm(team_name: str) -> dict:
    model = get_model()

    prompt = f"""
You are a sports data generator.

Task:
Generate a realistic team for: {team_name}

Requirements:
- Include 5 to 8 players
- Each player must have:
  - name
  - role (Forward, Midfielder, Defender)
  - score (integer between 60 and 100)

Output:
Return ONLY a valid JSON object like:
{{
  "name": "{team_name}",
  "players": [
    {{
      "name": "...",
      "role": "...",
      "score": ...
    }}
  ]
}}

Do NOT include any text before or after the JSON.
Do NOT use markdown or code blocks.
"""

    try:
        response = model.invoke(prompt)
        content = response.content

        # Extract JSON
        json_match = re.search(r"\{.*\}", content, re.DOTALL)

        if not json_match:
            raise ValueError("No JSON found in LLM response")

        json_str = json_match.group()

        team = json.loads(json_str)

        return team

    except Exception as e:
        print(f"Team generation error: {e}")

        # Fallback minimal
        return {
            "name": team_name,
            "players": [
                {"name": "Fallback Player", "role": "Midfielder", "score": 70}
            ]
        }

if __name__ == "__main__":
    team_name = input("Enter team name: ")
    team = generate_team_from_llm(team_name)

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
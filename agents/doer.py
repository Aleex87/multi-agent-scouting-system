from utils.logger import log
from utils.models import get_model
import re
import json


class DoerAgent:
    def __init__(self):
        self.model = get_model()

    def run(self, plan: dict) -> dict:
        log("Doer: searching for candidate player using LLM")

        
        target_role = plan["target_role"]

        prompt = f"""
You are a scouting agent.

Task:
Find a suitable player for the following role: {target_role}

Requirements:
- The player should fit the role
- Assign a value between 60 and 100
- The player can be real or fictional

Output:
Return ONLY a valid JSON object like:
{{
  "candidate": {{
    "name": "...",
    "role": "...",
    "value": ...
  }},
  "reason": "..."
}}
"""

        try:
            response = self.model.invoke(prompt)
            content = response.content

            log(f"LLM raw output: {content}")

            # Extract JSON block from response
            json_match = re.search(r"\{.*\}", content, re.DOTALL)

            if not json_match:
                raise ValueError("No JSON found in LLM response")

            json_str = json_match.group()

            parsed = json.loads(json_str)

            log(f"Doer result (LLM): {parsed}")
            return parsed

        except Exception as e:
            log(f"Doer error: {e}")

            return {
                "candidate": {
                    "name": "Fallback Player",
                    "role": target_role,
                    "value": 70
                },
                "reason": "Fallback due to LLM error"
            }

        # Originally implemented as a deterministic stub during system design.
        # This component has been upgraded to use an LLM for candidate generation.
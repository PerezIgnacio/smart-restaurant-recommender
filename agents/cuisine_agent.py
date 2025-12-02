import json

from .base_agent import BaseAgent
from .states import RestaurantRecommendationState

class CuisineAgent(BaseAgent):
    SYSTEM_PROMPT = """
    You are the Cuisine Agent.
    Extract the most likely cuisine preferences from the user query.

    Respond ONLY in the format:
    { "cuisines": ["cuisine1", "cuisine2"] }
    """

    def run(self, state: RestaurantRecommendationState):
        user_prompt = f'User Query: "{state["user_query"]}"'
        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ]

        raw = self.llm(messages)

        data = json.loads(raw)

        return {"cuisines": data["cuisines"]}

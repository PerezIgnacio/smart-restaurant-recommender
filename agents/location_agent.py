import json

from .base_agent import BaseAgent
from .states import RestaurantRecommendationState

class LocationAgent(BaseAgent):
    SYSTEM_PROMPT = """
    You are the Location Agent.
    
    Your job is to extract real U.S. cities + states explicitly or implicitly mentioned in the user query.
    
    Return ONLY cities in the format:
    { "locations": ["City, ST"] }
    
    STRICT RULES:
    1. A valid location MUST be a real U.S. city.
       - If it's not a real city, DO NOT guess.
    2. NEVER treat neighborhoods, districts, or areas as cities.
    3. If the query mentions only a neighborhood (e.g., "downtown Chicago"), extract the REAL city:
       - "downtown Chicago" → ["Chicago, IL"]
    4. If a city is mentioned without a state, infer its correct U.S. state:
       - Nashville → Nashville, TN
       - Chicago → Chicago, IL
    5. If multiple real cities appear, return all.
    6. Output ONLY valid JSON. No explanations.
    
    Example valid output:
    { "locations": ["Chicago, IL", "Nashville, TN"] }
    """

    def run(self, state: RestaurantRecommendationState):
        user_prompt = f'User Query: "{state["user_query"]}"'

        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ]

        raw = self.llm(messages)

        data = json.loads(raw)

        return {"locations": data["locations"]}
    
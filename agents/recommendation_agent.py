from .base_agent import BaseAgent
from .states import RestaurantRecommendationState

class RecommendationAgent(BaseAgent):
    SYSTEM_PROMPT = """
    You are the Recommendation Agent.
    
    Your job:
    Given (1) the user query, (2) inferred user preferences, and (3) a list of candidate restaurants,
    recommend up to 3 restaurants that best match what the user is looking for.
    
    STRICT RULES:
    1. You MUST use the inferred preferences (cuisines + locations) when scoring and ranking options.
    2. You MUST NOT reveal or explicitly mention the inferred preferences.
    3. Speak directly to the user. Do NOT refer to them in third person ("the user").
    4. DO NOT return more than 3 recommendations.
    5. Explanations must ONLY reference:
       - The original user query.
       - Details found in each restaurant (name, cuisine, rating, review content, etc.)
    6. Return the restaurant recommendations sorted by score descending. Use the following format for each:
        **{name}**
        - Match reason: {explanation}
        - Score: {X}/10
    """

    def __init__(self, embedder, index, reranker, client, model="gpt-4o"):
        self.embedder = embedder
        self.index = index
        self.reranker = reranker
        self.client = client
        self.model = model

    def run(self, state: RestaurantRecommendationState):
        # Add cuisines + location to query
        faiss_query = state["user_query"]
        if state.get("cuisines"):
            faiss_query += " Cuisines: " + " ".join(state["cuisines"])
        if state.get("locations"):
            faiss_query += " Locations: " + " ".join(state["locations"])

        # RAG
        search_result = self.rag(faiss_query)

        # Context for LLM
        user_prompt = f"""
        User Query: "{state['user_query']}"

        Inferred User preferences:
        - Cuisines: {state.get('cuisines')}
        - Locations: {state.get('locations')}

        Restaurants information:
        {search_result}
        """

        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ]

        response = self.llm(messages)

        return {"recommendations": response}
    
    def rag(self, query):
        query_embedding = self.embedder.encode_query(query)

        # Stage 1: FAISS retrieval
        stage1 = self.index.search(query_embedding, k=25)

        # Stage 2: Reranker
        stage2 = self.reranker.rerank(query, stage1, top_k=5)

        search_result = "\n".join([doc["text"] for doc in stage2])

        return search_result
        

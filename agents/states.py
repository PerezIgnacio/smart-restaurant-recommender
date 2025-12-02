from typing import TypedDict, Optional, List

class RestaurantRecommendationState(TypedDict):
    user_query: str
    cuisines: Optional[List[str]]
    locations: Optional[List[str]]
    recommendations: str

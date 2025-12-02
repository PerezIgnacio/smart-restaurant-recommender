import json
from collections import defaultdict
from typing import List, Dict

DATA_DIR = "data"

def load_businesses() -> List[Dict]:
    business_file = f"{DATA_DIR}/yelp_academic_dataset_business.json"
    restaurants = []

    print("Loading businesses...")

    with open(business_file, "r", encoding="utf8") as f:
        for line in f:
            business = json.loads(line)

            # Only restaurants
            categories = business.get("categories") or ""
            if "Restaurants" in categories:
                restaurants.append({
                    "business_id": business["business_id"],
                    "name": business["name"],
                    "city": business["city"],
                    "state": business["state"],
                    "categories": categories,
                    "rating": business.get("stars", 0),
                })

    print("Restaurants found:", len(restaurants))
    return restaurants


def load_reviews(max_reviews_per_business: int = 5) -> Dict[str, List[str]]:
    review_file = f"{DATA_DIR}/yelp_academic_dataset_review.json"
    reviews_by_business = defaultdict(list)

    print("Loading reviews...")

    with open(review_file, "r", encoding="utf8") as f:
        for line in f:
            review = json.loads(line)
            b_id = review["business_id"]

            if len(reviews_by_business[b_id]) < max_reviews_per_business:
                reviews_by_business[b_id].append(review["text"])

    print("Total restaurants with reviews:", len(reviews_by_business))
    return reviews_by_business

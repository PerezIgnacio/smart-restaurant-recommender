from typing import List, Dict

def build_documents(
    restaurants: List[Dict],
    reviews_by_business: Dict[str, List[str]]
) -> List[Dict]:

    docs = []

    print("Building documents...")

    for restaurant in restaurants:
        r_id = restaurant["business_id"]
        reviews = reviews_by_business.get(r_id, [])

        doc_text = (
            f"Name: {restaurant['name']}. "
            f"Location: {restaurant['city']}, {restaurant['state']}. "
            f"Categories: {restaurant.get('categories') or ''}. "
            f"Rating: {restaurant['rating']}. "
            f"Reviews: {' '.join(reviews)}"
        ).strip()

        docs.append({
            "id": r_id,
            "text": doc_text,
        })

    print("Total documents:", len(docs))
    return docs

# Smart Restaurant Recommender

A small demo project showcasing the use of RAG (Retrieval-Augmented Generation) with multiple agents to recommend restaurants based on user preferences, cuisines, and location.

## Features
- Uses RAG to combine information retrieval with LLMs.
- Supports multiple agents to reason over user preferences.
- Demonstrates practical integration with real-world restaurant data.

## Getting Started

1. Clone the repo.
2. Copy the `.env.example` file to `.env`, and add your OpenAI key.
3. Install dependencies with `pip install -r requirements.txt`.
4. Download the JSON dataset from [Yelp Open Dataset](https://www.yelp.com/dataset).
5. Move the `business.json` and `review.json` files to the `data` folder in the repo.
6. Run the notebook with `jupyter notebook main.ipynb`

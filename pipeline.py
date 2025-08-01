import argparse
import json
import os
from ingest_products import fetch_products, save_raw_products
from describer import generate_description

def load_products(filepath="data/raw/products.json"):
    with open(filepath) as f:
        return json.load(f)

def save_descriptions(descriptions, filepath="data/descriptions/descriptions.json"):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(descriptions, f, indent=2)

def main(category_filter=None):
    products = fetch_products()
    save_raw_products(products)

    if category_filter:
        products = [p for p in products if p["category"].lower() == category_filter.lower()]
    
    results = []
    for product in products:
        description = generate_description(product)
        results.append({
            "title": product["title"],
            "category": product["category"],
            "price": product["price"],
            "rating": product["rating"],
            "description": description
        })
    
    save_descriptions(results)
    print(f"Saved {len(results)} descriptions to data/descriptions/descriptions.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--category", type=str, help="Filter products by category")
    args = parser.parse_args()
    main(args.category)

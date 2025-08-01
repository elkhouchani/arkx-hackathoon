import cohere
import os
import json
from dotenv import load_dotenv

load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
co = cohere.Client(COHERE_API_KEY)

with open("data/raw/products.json", "r") as f:
    products = json.load(f)


def generate_description(product: dict) -> str:
    
    prompt = f"""You are a structured content generator. Generate a detailed product description page in Markdown using the JSON input provided. Follow the exact content structure and formatting shown below.

Always assume the brand is "Unknown" unless provided. Return only the Markdown string. Do not include JSON or extra explanation.

Output format (Markdown):

![product name](https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400)

# Red Lipstick

**Category:** beauty  
**Price:** $12.99  
**Brand:** Unknown

## Overview  
The Red Lipstick is a classic and bold choice for adding a pop of color to your lips. With a creamy and pigmented formula, it provides a vibrant and long-lasting finish.

## Key Features  
- Creamy texture  
- Bold pigment  
- Long-lasting color  

## Why You'll Love It  
- Adds an instant pop to any look  
- Smooth application and vibrant payoff  
- Stays in place without drying out lips  

## How to Use  
- Apply directly to clean lips  
- For sharper edges, use a lip liner beforehand  
- Reapply as needed throughout the day  

## Customer Reviews  
> “Gorgeous color and super long-lasting!”  
> “Goes on smooth and feels luxurious.”

## Perfect For  
- Special occasions  
- Everyday confidence boost  
- Anyone who loves a bold lip

Input:
{json.dumps(product, indent=2)}

Output:
"""

    response = co.generate(
        model="command-r-plus",
        prompt=prompt
    )

    return response.generations[0].text.strip()

# Generate and save Markdown for each product
output_dir = "data/generated_descriptions"
os.makedirs(output_dir, exist_ok=True)

for product in products:
    markdown_description = generate_description(product)
    product_id = product.get("id", "unknown")
    file_path = os.path.join(output_dir, f"product_{product_id}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown_description)
    print(f"✅ Description generated for product {product_id}")
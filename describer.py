import cohere
import os
COHERE_API_KEY ="IQqvMnz3IdjblhKBs4PGz4jYEnkqr3FLz7LQKL8f"
co = cohere.Client(COHERE_API_KEY)
# response = co.chat(
#     model="command-a-03-2025", 
#     messages=[{"role": "user", "content": "hello world!"}]
# )
# print(response)
def generate_description(title,price,category,rating):
    prompt = f"Write a short, engaging product description for {category} named {title} priced at ${price}, with a rating of {rating} stars."

    response = co.generate(
        model="command-r-plus",
        prompt=prompt
    )
    return response.generations[0].text.strip()


description = generate_description("UltraFast Laptop", 999, "laptops", 4.7)
print("Generated Description:\n", description)
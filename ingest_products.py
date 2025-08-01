# ingest_products.py
import requests # For making web requests
import os       # For interacting with the file system (creating folders)
import json     # For working with JSON data

# Main function to fetch and save product data
# It now accepts 'num_products' as an argument, with a default value of 10
def ingest_products(num_products=10):
    
    # List to store filtered product data
    filtered_products = [] 

    # API URL now uses the 'num_products' argument
    api_url = f"https://dummyjson.com/products?limit={num_products}" 
    
    print(f"Getting {num_products} products from: {api_url}") # Updated print message
    
    # --- Fetching products from API ---
    try:
        response = requests.get(api_url)
        response.raise_for_status() # Check for HTTP errors
        
        data = response.json() # Parse JSON response
        all_fetched_products = data["products"] # Get list of products
        print(f"Successfully fetched {len(all_fetched_products)} products.")
        
        # Filter product details to keep only desired fields
        for product in all_fetched_products:
            filtered_product = {
                "id": product.get("id"),
                "title": product.get("title"),
                "description": product.get("description"),
                "category": product.get("category"),
                "price": product.get("price") ,
                "images": product.get("images") ,
            }
            filtered_products.append(filtered_product)
        
        products = filtered_products # Use filtered list for saving
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching products: {e}")
        print("Please check your internet connection or the API URL.")
        return None, [] # Return empty on error

    # --- Saving products to file ---
    # Create data/raw directory if it doesn't exist
    os.makedirs("data/raw", exist_ok=True)
    filename = os.path.join("data", "raw", "products.json") # Define output file path

    try:
        with open(filename, "w", encoding='utf-8') as f: # Open file for writing
            json.dump(products, f, indent=4) # Save filtered products as JSON
        print(f"Saved {len(products)} filtered products to: {filename}")
    except IOError as e:
        print(f"Error saving products to {filename}: {e}")
        return None, products # Return None if saving failed

    return filename, products # Return saved filename and product list

 

ingest_products()

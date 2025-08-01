# ArkX Hackathon Product Pipeline

## Overview
This project fetches product data from a public API, generates AI-based descriptions using the Cohere API, converts the descriptions to JSON, and provides a simple CLI pipeline for filtering by category.

## Prerequisites
- Python 3.8+
- Cohere API key (set as `COHERE_API_KEY` env var or in code)

## Installation
```bash
pip install -r requirements.txt
```

## Usage
1. Ingest raw product data:
   ```bash
   python ingest_products.py
   ```
2. Generate AI descriptions:
   ```bash
   python describer.py
   ```
3. Convert Markdown descriptions to JSON:
   ```bash
   python pipeline.py --category <optional_category>
   ```

## Team 2 Structure & Workflow Plan
| Step | Task | Steps | Input | Output | Deliverables |
| --- | --- | --- | --- | --- | --- |
| 1. Data Ingestion – NAIMA | Fetch 10 fake products from API and save locally | - Use `requests` to call API  
- Parse JSON response  
- Save to `data/raw/products.json` | - API endpoint: `https://dummyjson.com/products` | - JSON file: `data/raw/products.json`  
- Format: list of 10 product dicts | - `ingest_products.py`  
- Output: `data/raw/products.json` |
| 2. Description Generator – SIHAM | Generate AI-based descriptions using Cohere | - Load products from raw JSON  
- Create prompt for each product  
- Send to Cohere API  
- Save results to `data/descriptions/` | - File: `data/raw/products.json` | - Files: `data/descriptions/*.md`  - One per product | - `describer.py`  
- Function: `generate_description(product)` |
| 3. Pipeline Integration – HOUSSAM | Connect all steps and support `--category` filter | - Load raw data  
- (Optional) filter by category  
- Call description generator  
- Save outputs  
- Generate summary (bonus) | - `data/raw/products.json`  
- CLI arg: `--category` (optional) | - Folder: `data/descriptions/`  
- File: JSON via converter | - `pipeline.py`  
- Supports CLI |
| 4. Documentation & Styling – OUSSAMA | Write the README and make the final output pretty | - Document setup and team roles  
- Create styled Markdown/HTML output grouped by category | - Output files from previous steps  
- Team info and structure | - `README.md`  
- (Bonus) styled product display | 

## File Structure
```
├── data/
│   ├── raw/products.json
│   ├── generated_descriptions/
│   └── products_in_json/output.json
├── ingest_products.py
├── describer.py
├── pipeline.py
├── markdown_to_json_converter.py
├── requirements.txt
└── README.md
```

## Configuration
Set your Cohere API key:
```bash
export COHERE_API_KEY="your_api_key_here"
```

## License
MIT

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

## 🚀 Team 2 Structure & Workflow Plan

| Step | Task | Workflow | Input | Output | Deliverables |
|------|------|----------|--------|--------|--------------|
| **1. Data Ingestion – NAIMA** | Fetch 10 fake products from API and save locally | - Use `requests` to call API<br>- Parse JSON response<br>- Save to `data/raw/products.json` | - API endpoint: `https://dummyjson.com/products` | - JSON file: `data/raw/products.json`<br>- Format: list of 10 product dictionaries | - Script: `ingest_products.py`<br>- Output file: `data/raw/products.json` |
| **2. Description Generator – SIHAM** | Generate AI-based descriptions using Cohere | - Load products from raw JSON<br>- Create prompt for each product<br>- Send to Cohere API<br>- Save results to `data/descriptions/` | - File: `data/raw/products.json` | - Files: `data/descriptions/*.md`<br>- One Markdown file per product | - Script: `describer.py`<br>- Function: `generate_description(product)` |
| **3. Pipeline Integration – HOUSSAM** | Connect all steps and support `--category` filter | - Load raw data<br>- (Optional) filter by category<br>- Call description generator<br>- Save outputs<br>- Generate summary (bonus) | - File: `data/raw/products.json`<br>- CLI arg: `--category` (optional) | - Folder: `data/descriptions/`<br>- Final JSON or structured output | - Script: `pipeline.py`<br>- CLI support |
| **4. Documentation & Styling – OUSSAMA** | Write the README and make the final output pretty | - Document setup and team roles<br>- Create styled Markdown/HTML output grouped by category | - Output files from previous steps<br>- Team info and structure | - `README.md`<br>- (Bonus) Styled product display | - This file (`README.md`)<br>- Optional styled output viewer |


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

## Run project
Serve via Local HTTP Server (Use Python’s built-in HTTP server to simulate a web environment)
In the root directory of the project, run:
```bash
python -m http.server 8000
```
Then open your browser and go to:

```bash
http://localhost:8000/product_page.html
```

## License
MIT

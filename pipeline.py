import logging
from ingest_products import ingest_products
from describer import generate_all_descriptions
from markdown_to_json_converter import export_markdown_as_json


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )


def main():
    setup_logging()
    logging.info("🚀 Starting product pipeline...")

    try:
        # Step 1: Ingest raw product data (optional)
        ingest_products()
        logging.info("🗂️  Raw product data ingested successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to ingest products: {e}")

    try:
        # Step 2: Generate descriptions
        generate_all_descriptions()
        logging.info("📝 Product descriptions generated successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to generate descriptions: {e}")

    try:
        # Step 3: Convert markdown to JSON
        export_markdown_as_json()
        logging.info("📦 Markdown converted to JSON successfully.")
    except Exception as e:
        logging.error(f"❌ Failed to export markdown as JSON: {e}")

    logging.info("✅ Pipeline completed.")


if __name__ == "__main__":
    main()

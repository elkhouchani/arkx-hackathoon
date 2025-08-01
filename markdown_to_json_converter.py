import os
import json

# === Global Configuration ===
MARKDOWN_INPUT_FOLDER = "./data/generated_descriptions"
JSON_OUTPUT_FILE = "./data/products_in_json/output.json"


def get_sorted_markdown_files(directory: str) -> list[str]:
    """
    Return a sorted list of Markdown (.md) filenames in the given directory.
    Raises FileNotFoundError if the directory doesn't exist.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"📁 Input folder does not exist: {directory}")

    return sorted([f for f in os.listdir(directory) if f.endswith('.md')])


def parse_markdown_files_to_json(directory: str) -> list[dict]:
    """
    Read all Markdown files in a directory and return a list of dicts
    with 'id' and 'md' content.
    """
    markdown_data = []
    for filename in get_sorted_markdown_files(directory):
        file_id = os.path.splitext(filename)[0]
        filepath = os.path.join(directory, filename)

        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        markdown_data.append({
            "id": file_id,
            "md": content
        })

    return markdown_data


def ensure_directory_exists(path: str):
    """
    Ensure that a directory exists; create it if it doesn't.
    """
    os.makedirs(path, exist_ok=True)


def export_markdown_as_json():
    """
    Convert Markdown files in the configured folder to a structured JSON file.
    """
    markdown_data = parse_markdown_files_to_json(MARKDOWN_INPUT_FOLDER)
    output_dir = os.path.dirname(JSON_OUTPUT_FILE)
    ensure_directory_exists(output_dir)

    with open(JSON_OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(markdown_data, f, indent=2, ensure_ascii=False)

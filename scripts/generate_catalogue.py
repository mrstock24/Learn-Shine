from pathlib import Path
import json

# Find the repository's books folder.
BOOKS_DIR = Path("books")
OUTPUT_FILE = Path("library.json")

books = []

# Search through books/ and every folder inside it.
for file_path in BOOKS_DIR.rglob("*"):
    if not file_path.is_file():
        continue

    # Only include PDF and EPUB files.
    if file_path.suffix.lower() not in {".pdf", ".epub"}:
        continue

    # Use the first folder under books/ as the category.
    relative_path = file_path.relative_to(BOOKS_DIR)
    category = relative_path.parts[0] if len(relative_path.parts) > 1 else "Uncategorised"

    books.append({
        "title": file_path.stem,
        "category": category,
        "path": file_path.as_posix()
    })

# Sort books alphabetically.
books.sort(key=lambda book: book["title"].lower())

# Create the catalogue.
OUTPUT_FILE.write_text(
    json.dumps(books, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print(f"Catalogue generated with {len(books)} books.")

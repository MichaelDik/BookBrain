import fitz  # PyMuPDF
import sqlite3
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text()
        pages.append((i + 1, text))
    return pages

def store_in_sqlite(book_title, pages, db_path="books.db"):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            page_number INTEGER,
            text TEXT
        )
    ''')

    # Insert pages
    for page_number, text in pages:
        c.execute('''
            INSERT INTO books (title, page_number, text)
            VALUES (?, ?, ?)
        ''', (book_title, page_number, text))

    conn.commit()
    conn.close()
    print(f"Stored {len(pages)} pages for '{book_title}' in {db_path}")

# --- Example usage ---

pdf_path = "/Users/mdik/BookBrain/Books/PrideandPrejudice.pdf"
book_title = os.path.splitext(os.path.basename(pdf_path))[0]  # e.g., "test"
pages = extract_text_from_pdf(pdf_path)
store_in_sqlite(book_title, pages)



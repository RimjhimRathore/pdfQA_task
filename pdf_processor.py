import fitz  # PyMuPDF

def extract_text(pdf_path: str) -> str:
    """Extract all text from a PDF file page by page."""
    doc = fitz.open(pdf_path)
    full_text = ""
    for page_num, page in enumerate(doc):
        full_text += page.get_text()
    doc.close()
    return full_text

def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50) -> list:
    """
    Split text into overlapping word-level chunks.
    Overlap prevents losing context at chunk boundaries.
    """
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        if chunk.strip():
            chunks.append(chunk)
        start += chunk_size - overlap
    return chunks
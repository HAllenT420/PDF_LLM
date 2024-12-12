# tests/test_ingestion.py
from src.data_ingestion.extract_text import extract_text_from_pdf

def test_extract_text_from_pdf():
    text = extract_text_from_pdf("data/pdfs/example.pdf")
    assert len(text) > 0

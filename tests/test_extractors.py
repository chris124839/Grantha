from pathlib import Path

from docx import Document
from backend.app import extract_pages


def test_extract_txt(tmp_path: Path):
    source = tmp_path / "sample.txt"
    source.write_text("namaste grantha", encoding="utf-8")
    assert extract_pages(source) == ["namaste grantha"]


def test_extract_docx(tmp_path: Path):
    source = tmp_path / "sample.docx"
    doc = Document()
    doc.add_paragraph("First paragraph")
    doc.add_paragraph("Second paragraph")
    doc.save(source)
    assert extract_pages(source) == ["First paragraph\nSecond paragraph"]

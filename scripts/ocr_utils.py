from bs4 import BeautifulSoup
import re
from PIL import Image
from pdf2image import convert_from_path

# HTML į tekstą
def html_to_text(html_content: str) -> str:
    soup = BeautifulSoup(html_content, "lxml")
    for s in soup(["script", "style"]):
        s.extract()
    text = soup.get_text(separator="\n")
    return re.sub(r"\n\s*\n+", "\n\n", text).strip()

# OCR iš paveikslėlio
def ocr_image_file(path):
    img = Image.open(path)
    import pytesseract
    return pytesseract.image_to_string(img, lang='eng')

# OCR iš PDF (pirmas 3 puslapiai)
def ocr_pdf_file(path):
    pages = convert_from_path(str(path), dpi=200, first_page=1, last_page=3)
    import pytesseract
    return "\n\n".join(pytesseract.image_to_string(p, lang='eng') for p in pages)

# Ištrauk pagrindines reikšmes iš teksto
def extract_basic_fields(text: str):
    date_match = re.search(r"Date[: ]+([0-9]{4}-[0-9]{2}-[0-9]{2}|[0-9]{2}/[0-9]{2}/[0-9]{4}|[0-9]{1,2} [A-Za-z]+ [0-9]{4})", text)
    total_match = re.search(r"(Total|TOTAL|Amount)[: ]+([0-9,.]+)", text)
    supplier_match = re.search(r"(Supplier|Vendor|From)[: ]+(.+)", text)
    return {
        "date": date_match.group(1) if date_match else None,
        "total": float(total_match.group(2).replace(",","")) if total_match else None,
        "supplier": supplier_match.group(2).strip() if supplier_match else None
    }

import requests
from bs4 import BeautifulSoup
import re
import pdfplumber

def fetch_pdf_text(pdf_url):
    resp = requests.get(pdf_url)
    resp.raise_for_status()
    with open("report.pdf", "wb") as f:
        f.write(resp.content)

    text = ""
    with pdfplumber.open("report.pdf") as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def fetch_beige_book_fed():
    # Latest Beige Book PDF (June 2025)
    return fetch_pdf_text(
        "https://www.federalreserve.gov/monetarypolicy/files/BeigeBook_20250604.pdf"
    )

def fetch_report_boe():
    # Bank of England Monetary Policy Report (May 2025)
    return fetch_pdf_text(
        "https://www.bankofengland.co.uk/-/media/boe/files/monetary-policy-report/2025/may/monetary-policy-report-may-2025.pdf"
    )

def fetch_bulletin_ecb():
    # ECB Economic Bulletin Issue 3 / 2025
    return fetch_pdf_text(
        "https://www.ecb.europa.eu/pub/pdf/ecbu/eb202503.en.pdf"
    )

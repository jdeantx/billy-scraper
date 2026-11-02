"""BillyScraper.py - PastPerfect Catalog Item Extractor
Copyright (c) 2026 James Dean
Licensed under the MIT License. See LICENSE in the project root for details.
This code cleaned up and validated with generative AI assistance.

Extracts metadata from Billy Ireland OSU Cartoon Library catalog records, formats them into a Markdown
table row, and copies the single row to the clipboard. Users can then paste that into a spreadsheet or
text file list.
"""

import sys
import subprocess
from urllib.parse import urlparse

# --- DEPENDENCY CHECKER FOR NON-TECHNICAL USERS ---
def ensure_dependencies() -> None:
    """Checks for required third-party packages and silently installs missing ones."""
    required_packages = {
        'requests': 'requests',
        'bs4': 'beautifulsoup4',
        'pyperclip': 'pyperclip',
    }

    missing_pip = []
    for module_name, pip_name in required_packages.items():
        try:
            __import__(module_name)
        except ImportError:
            missing_pip.append(pip_name)

    if missing_pip:
        print(f"Setting up required tools for first-time run ({', '.join(missing_pip)})... Please wait.")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", *missing_pip],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            print("Setup complete!\n")
        except subprocess.CalledProcessError:
            print(
                "\n[Notice] Automatic setup couldn't install dependencies automatically.",
                file=sys.stderr,
            )
            print(
                f"Please run this command in your terminal: {sys.executable} -m pip install {' '.join(missing_pip)}\n",
                file=sys.stderr,
            )

ensure_dependencies()

# --- MODULE IMPORTS ---
from dataclasses import dataclass
from bs4 import BeautifulSoup
import pyperclip
import requests

HEADERS = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/120.0.0.0 Safari/537.36'
    )
}


@dataclass
class CatalogRecord:
    title: str
    creator: str
    date: str
    finding_number: str
    collection: str
    version: str

    def to_markdown_row(self) -> str:
        """Formats the record as a single Markdown table row."""
        return (
            f"| {self.title} | {self.creator} | {self.date} | "
            f"{self.finding_number} | {self.collection} | {self.version} |"
        )


def fetch_and_parse(url: str) -> CatalogRecord | None:
    """Scrapes a PastPerfect web record and extracts only the target output fields."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=12)
        response.raise_for_status()
    except requests.RequestException as err:
        print(f"\n[Error] Could not fetch page details: {err}", file=sys.stderr)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    raw_data: dict[str, str] = {}

    # Extract title from main page headings as fallback
    title_elem = soup.find(['h1', 'h2']) or soup.find(class_='object-title')
    page_title = title_elem.get_text(strip=True) if title_elem else ''

    # Parse key-value pairs from standard table rows
    for row in soup.select('table tr, div.metadata-row, div.field-group'):
        cols = row.find_all(['td', 'th'])
        if len(cols) == 2:
            key = cols[0].get_text(strip=True).rstrip(':')
            val = cols[1].get_text(strip=True)
            if key and val:
                raw_data[key] = val

    # Parse key-value pairs from definition lists (<dl>/<dt>/<dd>)
    for dt in soup.find_all('dt'):
        dd = dt.find_next_sibling('dd')
        if dd:
            key = dt.get_text(strip=True).rstrip(':')
            val = dd.get_text(strip=True)
            if key and val:
                raw_data[key] = val

    # Direct mapping for exact output fields only
    title = raw_data.get('Title') or raw_data.get('Object Name') or page_title
    creator = raw_data.get('People') or raw_data.get('Creator') or raw_data.get('Artist', '')
    date = raw_data.get('Date', '')

    finding_number = (
        raw_data.get('Finding number') 
        or raw_data.get('Finding Number')
        or raw_data.get('Call Number')
        or raw_data.get('Object ID')
        or raw_data.get('Accession Number', '')
    )

    collection = raw_data.get('Collection', '')
    version = raw_data.get('Version') or raw_data.get('version', '')

    return CatalogRecord(
        title=title,
        creator=creator,
        date=date,
        finding_number=finding_number,
        collection=collection,
        version=version,
    )


def main() -> None:
    # Accept URL from command-line argument OR prompt the user interactively
    if len(sys.argv) > 1:
        target_url = sys.argv[1].strip()
    else:
        print("=== PastPerfect Catalog Item Extractor ===")
        target_url = input("\nPaste PastPerfect URL here and press Enter:\n> ").strip()

    parsed = urlparse(target_url)
    if not parsed.scheme or not parsed.netloc:
        print("\n[Error] Invalid web URL provided. It must start with http:// or https://")
        sys.exit(1)

    print("\nFetching record from catalog...")
    record = fetch_and_parse(target_url)

    if not record:
        sys.exit(1)

    header = "| Title | Creator | Date | Finding Number | Collection Name | Version |"
    divider = "| :--- | :--- | :---: | :--- | :--- | :---: |"
    row = record.to_markdown_row()

    print("\n" + "=" * 75)
    print("EXTRACTED RECORD PREVIEW:")
    print("=" * 75)
    print(header)
    print(divider)
    print(row)
    print("=" * 75)

    try:
        pyperclip.copy(row)
        print("\n✓ SUCCESS: Single row copied directly to your clipboard!")
        print("  Press Ctrl+V (or Cmd+V) to paste directly into your table.\n")
    except pyperclip.PyperclipException:
        print("\n[Notice] Could not access system clipboard automatically.")


if __name__ == '__main__':
    main()
    main()
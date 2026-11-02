# BillyScraper

**BillyScraper** is a lightweight Python utility designed to extract item metadata from PastPerfect Online catalog records (such as the OSU Billy Ireland Cartoon Library and Museum database) and format them into a clean, ready-to-paste Markdown table row. The formatted row is automatically copied directly to your computer's clipboard so you can paste it straight into your spreadsheet or text doc.

NOTE: This code was developed by a human, but validated and clean-up with AI assistance.

---

## Features
* **Zero Manual Setup:** Automatically installs required Python libraries ('requests', 'beautifulsoup4', 'pyperclip') on its first run.
* **Automatic Clipboard Copying:** Extracts item details and copies the single formatted row directly to your clipboard.
* **Smart Field Extraction:** Automatically locates 'Title', 'Creator', 'Date', 'Finding Number', 'Collection Name', and 'Version'.

---

## One-Time Setup (Prerequisites)

Before running BillyScraper for the first time, make sure Python is installed on your computer.

1. Download Python from [python.org/downloads](https://www.python.org/downloads/).
2. **Important for Windows users:** During installation, check the box at the bottom that says **"Add python.exe to PATH"** before clicking Install.

---

## How to Run BillyScraper

### Method 1: Interactive Prompt Mode (Easiest)

1. Open your terminal application:
   * **Windows:** Press the 'Windows Key', type 'cmd', and press **Enter**.
   * **Mac:** Press 'Cmd + Space', type 'terminal', and press **Enter**.

2. Launch the script:
   * **Windows:** 'py billyscraper.py'
   * **Mac:** 'python3 billyscraper.py'

3. When prompted, paste the URL of the catalog page you want to extract and press **Enter**:
   '''text
   Paste PastPerfect URL here and press Enter:
   > [https://osucartoons.pastperfectonline.com/webobject/690187DC-89EE-46B5-9BFE-930533934867](https://osucartoons.pastperfectonline.com/webobject/690187DC-89EE-46B5-9BFE-930533934867)
   '''

4. The script will fetch the record and copy the row. Switch to your document and press **Ctrl+V** (Windows) or **Cmd+V** (Mac) to paste!

---

### Method 2: Command Line Argument (Quick Mode)

You can pass the URL directly when launching the script:

'''bash
python3 billyscraper.py "[https://osucartoons.pastperfectonline.com/webobject/690187DC-89EE-46B5-9BFE-930533934867](https://osucartoons.pastperfectonline.com/webobject/690187DC-89EE-46B5-9BFE-930533934867)"
'''

---

## Output Example

When run against the Charles Burns *Circa: The Voyage of All Time* record ('https://osucartoons.pastperfectonline.com/webobject/690187DC-89EE-46B5-9BFE-930533934867'), BillyScraper generates:

'''text
| Title | Creator | Date | Finding Number | Collection Name | Version |
| :--- | :--- | :---: | :--- | :--- | :---: |
| Circa: The Voyage of All Time | Burns, Charles | 1989 | CGA.AC.CD6.009 | Jay Lynch Collection and Papers | Original Art |
'''

*(Note: The terminal displays both the headers and the row for visual preview, but only the raw data row is copied to your clipboard so your existing table remains intact.)*

---

## Step-by-Step Setup Guide

For a complete, beginner-friendly setup guide with drag-and-drop terminal instructions, see ['INSTRUCTIONS.md'](INSTRUCTIONS.md).

---

## Author and Acknowledgements

Created and maintained by James Dean.

This project is licensed under the [MIT License](LICENSE) - free for personal and commercial use.

'''

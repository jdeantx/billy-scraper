# How to Set Up and Run BillyScraper (Step-by-Step Instructions)

This guide will walk you through setting up and using **BillyScraper**, even if you have never used Python or terminal commands before.

---

## Step 1: Install Python (One-Time Setup)

If you don't already have Python installed on your computer:

1. Go to [python.org/downloads](https://www.python.org/downloads/) and click **Download Python**.
2. Run the downloaded installer.
3. **CRITICAL STEP FOR WINDOWS USERS:** On the very first installer screen, check the box at the bottom that says **"Add python.exe to PATH"** (or "Add Python to PATH"). If you miss this step, your computer will not know where to find Python when you run commands!
4. Click **Install Now** and complete the installation.

---

## Step 2: Download the Script

1. Download 'billyscraper.py' and place it in an easy-to-find location (such as your 'Documents' folder or Desktop).

---

## Step 3: Run BillyScraper

### On Windows:
1. Press the 'Windows Key', type 'cmd', and press **Enter** to open Command Prompt.
2. Type 'py ' (with a space after it). **Do not press Enter yet.**
3. Drag the 'billyscraper.py' file from your File Explorer and drop it directly into the Command Prompt window. The full path to the file will automatically appear.
4. Press **Enter**.

### On Mac:
1. Press 'Cmd + Space', type 'terminal', and press **Enter** to open Terminal.
2. Type 'python3 ' (with a space after it). **Do not press Enter yet.**
3. Drag the 'billyscraper.py' file from Finder and drop it directly into the Terminal window.
4. Press **Enter**.

---

## Step 4: Extract Catalog Details

1. When the terminal prompts you:
   '''text
   Paste PastPerfect URL here and press Enter:
   >
   '''
2. Copy the full web address of any item page from the catalog, for example:
   'https://osucartoons.pastperfectonline.com/webobject/690187DC-89EE-46B5-9BFE-930533934867'
3. Paste the URL into the terminal window ('Ctrl+V' or right-click on Windows, 'Cmd+V' on Mac) and press **Enter**.

---

## Step 5: Paste Your Results

Once the script finishes fetching the record, you will see a preview of the metadata followed by a confirmation message:

'''text
✓ SUCCESS: Single row copied directly to your clipboard!
'''

Open your Markdown file, research document, or spreadsheet, place your cursor where you want the new row, and press **Ctrl+V** (Windows) or **Cmd+V** (Mac) to paste the extracted row immediately!

'''

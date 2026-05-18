# 📘 DOCKET PDF STAMPING UTILITY — COMPLETE GUIDE
# Written for beginners — follow every step carefully

==============================================================
STEP 1: INSTALL PYTHON
==============================================================

1. Go to https://python.org/downloads
2. Download Python 3.11 or newer
3. During installation, CHECK the box that says "Add Python to PATH"
4. Click Install Now

To verify Python is installed:
   Open CMD → type: python --version
   You should see something like: Python 3.11.x


==============================================================
STEP 2: CREATE YOUR PROJECT FOLDER
==============================================================

1. Create a folder on your Desktop called: docket_project

2. Inside docket_project, create these folders:
   - input_pdfs
   - stamps
   (The rest will be auto-created by the code)

3. Copy these files into docket_project:
   - main.py
   - utils.py
   - requirements.txt


==============================================================
STEP 3: GET THE STAMP IMAGE
==============================================================

1. Download the stamp from the link given in the assignment:
   https://spawnventuresservices.sharepoint.com/...

2. Save it as: StampTNH.png

3. Place it inside your stamps/ folder

Your stamps/ folder should look like:
   stamps/
   └── StampTNH.png


==============================================================
STEP 4: ADD TEST PDF FILES
==============================================================

1. Create or find any PDF file (even a 1-page PDF is fine)
2. Place it inside the input_pdfs/ folder

For generating test PDFs:
   - Use any Word document → Save As → PDF
   - Or go to https://www.ilovepdf.com/ to create a sample PDF


==============================================================
STEP 5: INSTALL ALL REQUIRED LIBRARIES
==============================================================

1. Open CMD
2. Navigate to your project folder:
   cd Desktop\docket_project

3. Run this command:
   pip install -r requirements.txt

This will install:
   - pypdf         → reads and writes PDF files
   - reportlab     → draws the stamp onto a blank PDF page
   - Pillow        → handles image files (PNG/JPG)
   - openpyxl      → creates and writes Excel files
   - pyinstaller   → converts Python to .exe


==============================================================
STEP 6: RUN THE PROGRAM
==============================================================

1. In CMD (inside docket_project folder), run:
   python main.py

2. You will see live logs like:
   ============================================================
          DOCKET PDF STAMPING UTILITY — STARTED
   ============================================================
   Stamp validated successfully: stamps/StampTNH.png
   Found 2 PDF file(s) to process.
   [1/2] Processing: invoice_001.pdf
     SUCCESS → Saved to: Stamped Docs\invoice_001_stamped.pdf
   [2/2] Processing: contract.pdf
     SUCCESS → Saved to: Stamped Docs\contract_stamped.pdf
   ============================================================
         EXECUTION COMPLETE — FINAL SUMMARY
   ============================================================
     Total Files Found      : 2
     Successfully Stamped   : 2
     Failed                 : 0
   ============================================================

3. Check these outputs:
   - Stamped Docs/    → your stamped PDFs
   - reports/         → stamping_report.xlsx
   - logs/            → app.log


==============================================================
STEP 7: UNDERSTAND THE EXCEL REPORT
==============================================================

Open stamping_report.xlsx. It will have columns:

| File Name         | Stamped | Timestamp           | Remarks |
|-------------------|---------|---------------------|---------|
| invoice_001.pdf   | TRUE    | 2025-05-10 14:30:00 | Success |
| bad_file.pdf      | FALSE   | 2025-05-10 14:30:02 | Corrupted PDF |


==============================================================
STEP 8: BUILD THE .EXE FILE
==============================================================

In CMD (inside docket_project folder), run:
   pyinstaller --onefile --console main.py

This will create:
   dist/
   └── main.exe

Copy main.exe to your docket_project folder.
Double-click main.exe → CMD opens → program runs!

Make sure stamps/ and input_pdfs/ folders are in the SAME
folder as main.exe.


==============================================================
COMMON ERRORS AND FIXES
==============================================================

ERROR: "No module named 'pypdf'"
FIX: Run → pip install pypdf

ERROR: "Stamp file not found"
FIX: Make sure StampTNH.png is inside stamps/ folder

ERROR: "No PDF files found"
FIX: Make sure your PDFs are inside input_pdfs/ folder

ERROR: "Permission denied"
FIX: Close Adobe Reader or any program that has the PDF open


==============================================================
PROJECT FOLDER FINAL STRUCTURE (after running)
==============================================================

docket_project/
├── input_pdfs/
│   └── your_test.pdf
├── stamps/
│   └── StampTNH.png
├── Stamped Docs/                  ← auto-created
│   └── your_test_stamped.pdf      ← auto-created
├── reports/                       ← auto-created
│   └── stamping_report.xlsx       ← auto-created
├── logs/                          ← auto-created
│   └── app.log                    ← auto-created
├── dist/                          ← created by pyinstaller
│   └── main.exe
├── main.py
├── utils.py
└── requirements.txt

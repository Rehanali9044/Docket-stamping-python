import sys
import logging
from pathlib import Path

from utils import (
    setup_logging,
    get_pdfs,
    check_stamp,
    stamp_pdf,
    init_report,
    log_to_report
)

INPUT_FOLDER  = "input_pdfs"
STAMP_PATH    = "stamps/StampTNH.png"
OUTPUT_FOLDER = "Stamped Docs"
REPORT_PATH   = "reports/stamping_report.xlsx"
LOG_PATH      = "logs/app.log"


def main():
    for folder in [OUTPUT_FOLDER, "reports", "logs", INPUT_FOLDER, "stamps"]:
        Path(folder).mkdir(parents=True, exist_ok=True)

    setup_logging(LOG_PATH)
    log = logging.getLogger(__name__)

    print("\n===== PDF STAMPING STARTED =====\n")

    init_report(REPORT_PATH)

    try:
        check_stamp(STAMP_PATH)
        log.info(f"Stamp found: {STAMP_PATH}")
    except Exception as e:
        log.error(f"Stamp check failed: {e}")
        input("\nPress Enter to exit...")
        sys.exit(1)

    try:
        files = get_pdfs(INPUT_FOLDER)
    except Exception as e:
        log.error(str(e))
        input("\nPress Enter to exit...")
        sys.exit(1)

    total   = len(files)
    success = 0
    failed  = 0

    if total == 0:
        log.warning(f"No PDF files found in {INPUT_FOLDER}/")
        input("\nPress Enter to exit...")
        return

    log.info(f"Found {total} PDF(s) to process")

    for i, pdf in enumerate(files, 1):
        log.info(f"[{i}/{total}] Processing: {pdf.name}")

        try:
            out = stamp_pdf(pdf, STAMP_PATH, OUTPUT_FOLDER)
            log.info(f"Stamped successfully: {pdf.name}")
            log_to_report(REPORT_PATH, pdf.name, "TRUE", "Success")
            success += 1

        except FileNotFoundError:
            log.error(f"File not found: {pdf.name}")
            log_to_report(REPORT_PATH, pdf.name, "FALSE", "File not found")
            failed += 1

        except PermissionError:
            log.error(f"Permission denied: {pdf.name}")
            log_to_report(REPORT_PATH, pdf.name, "FALSE", "Permission denied")
            failed += 1

        except ValueError as e:
            msg = str(e)
            if "encrypted" in msg.lower():
                reason = "Encrypted PDF"
            elif "no pages" in msg.lower():
                reason = "Empty PDF"
            elif "corrupted" in msg.lower():
                reason = "Corrupted PDF"
            else:
                reason = msg
            log.error(f"{reason}: {pdf.name}")
            log_to_report(REPORT_PATH, pdf.name, "FALSE", reason)
            failed += 1

        except Exception as e:
            log.error(f"Unexpected error on {pdf.name}: {e}")
            log_to_report(REPORT_PATH, pdf.name, "FALSE", f"Error: {type(e).__name__}")
            failed += 1

    print("\n===== PROCESS COMPLETED =====")
    print(f"Total Files  : {total}")
    print(f"Successful   : {success}")
    print(f"Failed       : {failed}")
    print(f"Report saved : {REPORT_PATH}")
    print(f"Logs saved   : {LOG_PATH}")

    log.info(f"Done. Total: {total} | Success: {success} | Failed: {failed}")

    input("\nPress Enter to close...")


if __name__ == "__main__":
    main()
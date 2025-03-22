# Apple Report Parser

## Overview
This script processes Apple transaction reports in TXT format and generates a single CSV file with aggregated revenue per game and currency.

## 📂 Folder Structure
apple_report_parser/
│── data/
│   ├── input/                  # Place all Apple reports here
│   │   ├── report1.txt
│   │   ├── report2.txt
│   ├── output/                  # Folder for final output
│── main.py                      # Entry point
│── parser.py                    # Report processing logic
│── config.py                    # Game name mappings
│── requirements.txt              # Dependencies (if needed)
│── README.md                     # Usage guide

## Usage
1. **Place Apple reports (`.txt` files) inside** `data/input/`
2. **Run the script**:
   ```sh
   python3 main.py
# KenzLedger 🪙

A command-line personal finance and expense tracker built entirely on a mobile phone using Python, Termux, and Pydroid 3.

## ✨ Features
- Add income and expense transactions
- View current balance and net worth
- Generate category reports (split by income/expense)
- Delete transactions with a safety confirmation prompt
- **Data Persistence:** Your data is saved to a JSON file, so it survives app restarts!

## 🛠️ Tech Stack
- **Language:** Python 3
- **Storage:** JSON
- **Environment:** Termux, Pydroid 3 (Mobile Development)
- **Testing:** Python `unittest` module

## 🚀 How to Run
1. Clone the repository:
   `git clone https://github.com/KenzGlobe/kenzledger.git`
2. Navigate into the folder:
   `cd kenzledger`
3. Run the app:
   `python main.py`

## 🧪 Running Tests
To run the automated storage tests:
`python test_storage.py`

## 🏗️ Project Structure
- `main.py` - The entry point and menu loop
- `commands.py` - Feature logic (add, view, delete)
- `storage.py` - File I/O (load/save JSON)
- `kenz_ui.py` - Custom terminal UI styling
- `test_storage.py` - Automated unit tests

---
*Created by [KenzGlobe](https://github.com/KenzGlobe)*
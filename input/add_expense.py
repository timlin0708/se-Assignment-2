# input/add_expense.py
import csv
import os

DATA_FILE = "../data/expenses.csv"

def init_file():
    """Initialize CSV file if it does not exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "amount", "category", "note"])

def add_expense():
    """Prompt user for expense information and save it."""
    date = input("Date (YYYY-MM-DD): ")
    amount = input("Amount: ")
    category = input("Category: ")
    note = input("Note (optional): ")

    with open(DATA_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, category, note])

    print("Expense added.\n")

if __name__ == "__main__":
    init_file()
    while True:
        add_expense()
        cont = input("Add another expense? (y/n): ")
        if cont.lower() != "y":
            break

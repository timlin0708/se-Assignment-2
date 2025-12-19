# visualization/pie_chart.py
import csv
from collections import defaultdict
import matplotlib.pyplot as plt

DATA_FILE = "../data/expenses.csv"

def load_expenses():
    """Load expenses and sum by category."""
    totals = defaultdict(float)

    with open(DATA_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            totals[row["category"]] += float(row["amount"])

    return totals

def plot_pie_chart(totals):
    """Plot a pie chart of expenses by category."""
    categories = list(totals.keys())
    amounts = list(totals.values())

    plt.figure()
    plt.pie(amounts, labels=categories, autopct="%1.1f%%")
    plt.title("Expense Distribution by Category")
    plt.show()

if __name__ == "__main__":
    totals = load_expenses()
    plot_pie_chart(totals)

import csv
from collections import defaultdict
from datetime import datetime
import os

csv_file = "../day15/transactions.csv"

category_totals = defaultdict(lambda: {"income": 0, "expense": 0})

def load_transactions():
    if os.path.exists(csv_file):
        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                amount = float(row["Miktar"])
                trans_type = row["Tür"]
                category = row["Kategori"]
                if trans_type == "Gelir":
                    category_totals[category]["income"] += amount
                else:
                    category_totals[category]["expense"] += abs(amount)

def show_category_analysis():
    print("\n📊 Kategori Bazında Harcama Analizi:")
    total_income = 0
    total_expense = 0
    max_expense = 0
    max_category = ""

    for category, data in category_totals.items():
        income = data["income"]
        expense = data["expense"]
        net = income - expense
        total_income += income
        total_expense += expense

        if expense > max_expense:
            max_expense = expense
            max_category = category

        print(f"- {category} - Gelir: {income} TL, Gider: {expense} TL, Net: {net} TL")

    print("\n💰 Toplam Gelir:", total_income, "TL")
    print("💸 Toplam Gider:", total_expense, "TL")
    print("📈 Net Kazanç:", total_income - total_expense, "TL")
    print("🔴 En Çok Harcama Yapılan Kategori:", max_category, "-", max_expense, "TL")

def main():
    load_transactions()

    while True:
        print("\n--- Kişisel Finans Analiz Uygulaması (v5) ---")
        print("1. Kategori Bazında Harcama Analizi")
        print("2. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            show_category_analysis()

        elif choice == "2":
            print("Çıkılıyor... 👋")
            break

        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()

import csv
from collections import defaultdict
from datetime import datetime
import os

balance = 0
transactions = []
categories = ["Yemek", "Ulaşım", "Eğlence", "Fatura", "Diğer"]
category_totals = defaultdict(lambda: {"income": 0, "expense": 0})
csv_file = "transactions.csv"

def load_transactions():
    global balance
    if os.path.exists(csv_file):
        with open(csv_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                amount = float(row["Miktar"])
                trans_type = row["Tür"]
                category = row["Kategori"]
                if trans_type == "Gelir":
                    balance += amount
                    category_totals[category]["income"] += amount
                else:
                    balance -= amount
                    category_totals[category]["expense"] += abs(amount)
                transactions.append((amount, category, trans_type, row["Tarih"]))

def save_transaction(amount, category, trans_type):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(csv_file, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([now, trans_type, category, amount])

def add_income(amount, category):
    global balance
    balance += amount
    transactions.append((amount, category, "Gelir", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    category_totals[category]["income"] += amount
    save_transaction(amount, category, "Gelir")
    print(f"✅ {amount} TL gelir eklendi. Kategori: {category} - Güncel bakiye: {balance} TL")

def add_expense(amount, category):
    global balance
    balance -= amount
    transactions.append((-amount, category, "Gider", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    category_totals[category]["expense"] += amount
    save_transaction(-amount, category, "Gider")
    print(f"❌ {amount} TL gider eklendi. Kategori: {category} - Güncel bakiye: {balance} TL")

def choose_category():
    print("\n📂 Kategori Seçin:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    try:
        choice = int(input("Seçiminiz: ")) - 1
        if 0 <= choice < len(categories):
            return categories[choice]
        else:
            print("⚠️ Geçersiz kategori numarası.")
            return choose_category()
    except ValueError:
        print("⚠️ Lütfen geçerli bir sayı girin.")
        return choose_category()

def show_balance():
    print(f"\n🔍 Güncel Bakiye: {balance} TL")

def show_transactions():
    print("\n📋 Tüm İşlemler:")
    if not transactions:
        print("Henüz işlem yok.")
    else:
        for amount, category, trans_type, date in transactions:
            print(f"- {trans_type} ({amount} TL) - Kategori: {category} - Tarih: {date}")

def main():
    load_transactions()
    while True:
        print("\n--- Kişisel Finans Uygulaması (v4) ---")
        print("1. Gelir Ekle")
        print("2. Gider Ekle")
        print("3. Bakiye Görüntüle")
        print("4. Tüm İşlemleri Görüntüle")
        print("5. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            try:
                amount = float(input("Gelir miktarını girin: "))
                category = choose_category()
                add_income(amount, category)
            except ValueError:
                print("⚠️ Lütfen geçerli bir sayı girin.")

        elif choice == "2":
            try:
                amount = float(input("Gider miktarını girin: "))
                category = choose_category()
                add_expense(amount, category)
            except ValueError:
                print("⚠️ Lütfen geçerli bir sayı girin.")

        elif choice == "3":
            show_balance()

        elif choice == "4":
            show_transactions()

        elif choice == "5":
            print("Çıkılıyor... 👋")
            break

        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()

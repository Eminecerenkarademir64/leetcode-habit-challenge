from collections import defaultdict

balance = 0
transactions = []
categories = ["Yemek", "Ulaşım", "Eğlence", "Fatura", "Diğer"]
category_totals = defaultdict(lambda: {"income": 0, "expense": 0})

def add_income(amount, category):
    global balance
    balance += amount
    transactions.append((amount, category, "Gelir"))
    category_totals[category]["income"] += amount
    print(f"✅ {amount} TL gelir eklendi. Kategori: {category} - Güncel bakiye: {balance} TL")

def add_expense(amount, category):
    global balance
    balance -= amount
    transactions.append((-amount, category, "Gider"))
    category_totals[category]["expense"] += amount
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
        for amount, category, trans_type in transactions:
            print(f"- {trans_type} ({amount} TL) - Kategori: {category}")

def show_category_report():
    print("\n📊 Kategori Bazında Rapor:")
    for category, data in category_totals.items():
        total_income = data["income"]
        total_expense = data["expense"]
        net = total_income - total_expense
        print(f"- {category} - Gelir: {total_income} TL, Gider: {total_expense} TL, Net: {net} TL")

def main():
    while True:
        print("\n--- Kişisel Finans Uygulaması (v3) ---")
        print("1. Gelir Ekle")
        print("2. Gider Ekle")
        print("3. Bakiye Görüntüle")
        print("4. Tüm İşlemleri Görüntüle")
        print("5. Kategori Bazında Rapor")
        print("6. Çıkış")

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
            show_category_report()

        elif choice == "6":
            print("Çıkılıyor... 👋")
            break

        else:
            print("⚠️ Geçersiz seçim.")

if __name__ == "__main__":
    main()

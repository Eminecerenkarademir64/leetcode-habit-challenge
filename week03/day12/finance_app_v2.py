balance = 0
transactions = []

categories = ["Yemek", "Ulaşım", "Eğlence", "Fatura", "Diğer"]

def add_income(amount, category):
    global balance
    balance += amount
    transactions.append(f"Gelir (+{amount} TL) - Kategori: {category}")
    print(f"✅ {amount} TL gelir eklendi. Kategori: {category} - Güncel bakiye: {balance} TL")

def add_expense(amount, category):
    global balance
    balance -= amount
    transactions.append(f"Gider (-{amount} TL) - Kategori: {category}")
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
        for transaction in transactions:
            print(f"- {transaction}")

def main():
    while True:
        print("\n--- Kişisel Finans Uygulaması (v2) ---")
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

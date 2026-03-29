"""
mini-inventory v0 — Basitlestirilmis implementasyon
Ogrenci: Tunahan Caner YILDIZ (251478112)

Kapsam:
- init komutu calisir
- add komutu calisir

Sinirlamalar:
- Dongu ve liste kullanilmadi
- list, update ve delete komutlari henuz implemente edilmedi
"""

import sys
import os


def initialize():
    """Sistem klasorunu ve bos veri dosyasini olusturur."""
    if os.path.exists(".miniinventory"):
        return "Already initialized"

    os.mkdir(".miniinventory")

    file_object = open(".miniinventory/inventory.dat", "w")
    file_object.close()

    return "Initialized empty mini-inventory in .miniinventory/"


def is_valid_quantity(quantity_text):
    """Miktar bilgisinin negatif olmayan bir tam sayi olup olmadigini kontrol eder."""
    return quantity_text.isdigit()


def add_product(name, quantity_text):
    """Yeni bir urunu veri dosyasina ekler."""
    if not os.path.exists(".miniinventory"):
        return "Not initialized. Run: python solution_v0.py init"

    if not is_valid_quantity(quantity_text):
        return "Invalid quantity"

    file_object = open(".miniinventory/inventory.dat", "r")
    content = file_object.read()
    file_object.close()

    if content == "":
        product_id = 1
    else:
        product_id = content.count("\n") + 1

    file_object = open(".miniinventory/inventory.dat", "a")
    file_object.write(str(product_id) + "|" + name + "|" + quantity_text + "|2026-03-15\n")
    file_object.close()

    return "Added product #" + str(product_id) + ": " + name + " (" + quantity_text + ")"


def show_not_implemented(command_name):
    """Henuz gelistirilmemis komutlar icin bilgilendirme mesaji dondurur."""
    return "Command '" + command_name + "' will be implemented in future weeks."


if len(sys.argv) < 2:
    print("Usage: python solution_v0.py <command> [args]")

elif sys.argv[1] == "init":
    print(initialize())

elif sys.argv[1] == "add":
    if len(sys.argv) < 4:
        print("Usage: python solution_v0.py add <name> <quantity>")
    else:
        print(add_product(sys.argv[2], sys.argv[3]))

elif sys.argv[1] == "list":
    print(show_not_implemented("list"))

elif sys.argv[1] == "update":
    print(show_not_implemented("update"))

elif sys.argv[1] == "delete":
    print(show_not_implemented("delete"))

else:
    print("Unknown command: " + sys.argv[1])
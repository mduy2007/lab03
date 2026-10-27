from models import Product, Inventory

if __name__ == "__main__":
    inv = Inventory()
    inv.add(Product("P01", "Pen", 5_000, 100))
    inv.add(Product("P02", "Notebook", 15_000, 40))
    inv.add(Product("P03", "Ruler", 8_000, 3))
    
    inv.export_stock("P01", 30)
    inv.import_stock("P03", 10)
    
    # In kết quả
    print(len(inv), "P02" in inv, f"{inv.total_value:,.0f}.")
    print([p.name for p in inv.search("no")], [p.name for p in inv.low_stock(20)])
    
    for action in (lambda: inv.export_stock("P02", 50),
                   lambda: inv.add(Product("P01", "Pen 2", 1, 1))):
        try:
            action()
        except ValueError as e:
            print("Error:", e)
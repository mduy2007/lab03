from models import Product, Inventory

def main():
    inv = Inventory()

    while True:
        print("\n--- QUẢN LÝ KHO HÀNG ---")
        print("1. Thêm hàng")
        print("2. Nhập kho")
        print("3. Xuất kho")
        print("4. Tìm kiếm")
        print("5. Báo cáo tồn kho")
        print("6. Hàng sắp hết")
        print("0. Thoát")
        
        choice = input("Chọn chức năng (0-6): ")
        
        try:
            if choice == '1':
                code = input("Nhập mã hàng: ")
                name = input("Nhập tên hàng: ")
                price = float(input("Nhập đơn giá: "))
                qty = int(input("Nhập số lượng: "))
                inv.add(Product(code, name, price, qty))
                print("Thêm thành công.")
                
            elif choice == '2':
                code = input("Nhập mã hàng cần nhập: ")
                qty = int(input("Nhập số lượng nhập thêm: "))
                inv.import_stock(code, qty)
                print("Nhập kho thành công.")
                
            elif choice == '3':
                code = input("Nhập mã hàng cần xuất: ")
                qty = int(input("Nhập số lượng xuất: "))
                inv.export_stock(code, qty)
                print("Xuất kho thành công.")
                
            elif choice == '4':
                keyword = input("Nhập từ khóa tìm kiếm: ")
                results = inv.search(keyword)
                if not results:
                    print("Không tìm thấy sản phẩm nào.")
                else:
                    for p in results:
                        print(p)
                        
            elif choice == '5':
                print("--- BÁO CÁO TỒN KHO ---")
                print(f"{'Mã':<6} | {'Tên hàng':<15} | {'Đơn giá':>10} | {'SL':>5} | {'Tổng giá trị':>12}")
                print("-" * 60)
                # Sắp xếp theo mã hàng cho đẹp
                for code in sorted(inv._Inventory__products.keys()):
                    print(inv._Inventory__products[code])
                print("-" * 60)
                print(f"Tổng giá trị toàn kho: {inv.total_value:,.0f} VNĐ")
                
            elif choice == '6':
                threshold = int(input("Nhập ngưỡng cảnh báo (mặc định 5): ") or 5)
                low_items = inv.low_stock(threshold)
                if not low_items:
                    print(f"Không có mặt hàng nào dưới ngưỡng {threshold}.")
                else:
                    print(f"Các mặt hàng sắp hết (SL <= {threshold}):")
                    for p in low_items:
                        print(p)
                        33
            elif choice == '0':
                print("Đã thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
                
        except ValueError as e:
            print(f"Lỗi dữ liệu: {e}")
        except KeyError as e:
            print(f"Lỗi: Không tìm thấy mã hàng {e}")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    main()
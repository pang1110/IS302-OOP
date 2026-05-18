#CalilungRRC
def add_product(product):
    with open("products.txt", "a") as file_rrc:
        file_rrc.write(product.get_product_info() + "\n")

        def view_products():
            try:
                with open("products.txt", "r") as file_rrc:
                    products_rrc = file_rrc.readlines()
                    for product in products_rrc:
                        print(product.strip())
            except FileNotFoundError:
                print("No products found.")
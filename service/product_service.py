from models.product import Product

class ProductService:
    def __init__(self, product_repo):
        self.product_repo = product_repo

    def get_product(self, product_id):
        return self.product_repo.get_by_id(product_id)

    def get_all(self):
        return self.product_repo.list_all()

    def create_product(self, nome, price):
        product = Product(name=nome, price=price)
        self.user_repo.add(product)
        return product

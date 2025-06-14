from models.customer import Customer

class CustomerService:
    def __init__(self, customer_repo):
        self.customer_repo = customer_repo

    def get_customer(self, customer_id):
        return self.customer_repo.get_by_id(customer_id)

    def get_all(self):
        return self.customer_repo.list_all()

    def create_customer(self, nome):
        customer = Customer(name=nome)
        self.customer_repo.add(customer)
        return customer

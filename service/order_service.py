from models.order import Order
from models.order_line import OrderLine
class OrderService:
    def __init__(self, order_repo):
        self.order_repo = order_repo

    def get_order(self, order_id):
        return self.order_repo.get_by_id(order_id)

    def get_all(self):
        return self.order_repo.list_all()

def create_order(self, customer_id, items):
    order = Order(customer_id=customer_id, order_date=datetime.utcnow())

    total = 0
    for item in items:
        product = self.product_repo.get_by_id(item['product_id'])
        if not product:
            raise ValueError(f"Produto {item['product_id']} não encontrado.")

        quantity = item['quantity']
        subtotal = product.price * quantity
        total += subtotal

        order_line = OrderLine(
            product_id=product.id,
            quantity=quantity
        )
        order.order_lines.append(order_line)

    order.total_amount = total
    self.order_repo.add(order)
    return order

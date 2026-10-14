from typing import Dict, List

from src.domain.models import Order, OrderItem
from src.use_cases.interfaces import IOrderRepository


class CreateOrderUseCase:
    def __init__(self, order_repo: IOrderRepository):
        self._order_repo = order_repo

    def execute(self, order_id: str, raw_items: List[Dict]) -> dict:
        items = [
            OrderItem(
                item_id=str(item["id"]),
                title=str(item["title"]),
                price=float(item["price"]),
                quantity=int(item["quantity"]),
            )
            for item in raw_items
        ]
        order = Order(order_id=order_id, items=items)
        self._order_repo.save(order)
        return {
            "order_id": order.order_id,
            "subtotal": order.calculate_subtotal(),
            "final_amount": order.calculate_final_amount(),
        }


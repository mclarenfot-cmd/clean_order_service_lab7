from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class OrderItem:
    item_id: str
    title: str
    price: float
    quantity: int

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("Цена позиции не может быть отрицательной.")
        if self.quantity <= 0:
            raise ValueError("Количество позиции должно быть больше нуля.")

    @property
    def total_price(self) -> float:
        return self.price * self.quantity


class Order:
    DISCOUNT_THRESHOLD = 5000.0
    DISCOUNT_RATE = 0.10

    def __init__(self, order_id: str, items: List[OrderItem]):
        if not order_id:
            raise ValueError("Идентификатор заказа обязателен.")
        if not items:
            raise ValueError("Заказ не может быть пустым.")
        self.order_id = order_id
        self._items = list(items)

    @property
    def items(self) -> List[OrderItem]:
        return list(self._items)

    def calculate_subtotal(self) -> float:
        return round(sum(item.total_price for item in self._items), 2)

    def calculate_final_amount(self) -> float:
        subtotal = self.calculate_subtotal()
        if subtotal >= self.DISCOUNT_THRESHOLD:
            return round(subtotal * (1 - self.DISCOUNT_RATE), 2)
        return subtotal


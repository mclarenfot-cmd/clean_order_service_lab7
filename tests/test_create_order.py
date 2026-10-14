import unittest

from src.infrastructure.memory_repo import InMemoryOrderRepository
from src.use_cases.create_order import CreateOrderUseCase


class TestCreateOrderUseCase(unittest.TestCase):
    def test_execute_saves_order_and_returns_totals(self):
        repo = InMemoryOrderRepository()
        use_case = CreateOrderUseCase(repo)

        result = use_case.execute(
            "ORD-100",
            [
                {"id": "A", "title": "Monitor", "price": 3000, "quantity": 1},
                {"id": "B", "title": "Keyboard", "price": 2500, "quantity": 1},
            ],
        )

        self.assertEqual(result["subtotal"], 5500.0)
        self.assertEqual(result["final_amount"], 4950.0)
        self.assertIsNotNone(repo.get_by_id("ORD-100"))


if __name__ == "__main__":
    unittest.main()


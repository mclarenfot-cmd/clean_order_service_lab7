from src.infrastructure.memory_repo import InMemoryOrderRepository
from src.use_cases.create_order import CreateOrderUseCase


def main() -> None:
    repository = InMemoryOrderRepository()
    use_case = CreateOrderUseCase(repository)
    result = use_case.execute(
        "ORD-001",
        [
            {"id": "1", "title": "Server Rack", "price": 4000.0, "quantity": 1},
            {"id": "2", "title": "Patch Cord", "price": 1500.0, "quantity": 1},
        ],
    )
    print(result)


if __name__ == "__main__":
    main()


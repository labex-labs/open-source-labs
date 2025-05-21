# 클래스 변수를 사용한 타입 유효성 검사 일치시키기

현재 `Stock` 클래스는 타입 처리를 위해 `_types` 클래스 변수와 property setter 를 모두 사용합니다. 일관성과 유지 관리성을 향상시키기 위해 이러한 메커니즘을 일치시켜 동일한 타입 정보를 사용하도록 합니다.

**지침:**

1.  에디터에서 `stock.py` 파일을 엽니다.

2.  `_types` 클래스 변수에 정의된 타입을 사용하도록 property setter 를 수정합니다.

    ```python
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Expected {self._types[1].__name__}")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Expected {self._types[2].__name__}")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value
    ```

3.  `stock.py` 파일을 저장합니다.

4.  `test_subclass.py`라는 테스트 스크립트를 만듭니다.

    ```bash
    touch /home/labex/project/test_subclass.py
    ```

5.  `test_subclass.py` 파일에 다음 코드를 추가합니다.

    ```python
    from stock import Stock
    from decimal import Decimal

    # Create a subclass with different types
    class DStock(Stock):
        _types = (str, int, Decimal)

    # Test the base class
    s = Stock('GOOG', 100, 490.10)
    print(f"Stock: {s.name}, Shares: {s.shares}, Price: {s.price}, Cost: {s.cost}")

    # Test valid update with float
    try:
        s.price = 500.25
        print(f"Updated Stock price: {s.price}, Cost: {s.cost}")
    except Exception as e:
        print(f"Error updating Stock price: {e}")

    # Test the subclass with Decimal
    ds = DStock('AAPL', 50, Decimal('142.50'))
    print(f"DStock: {ds.name}, Shares: {ds.shares}, Price: {ds.price}, Cost: {ds.cost}")

    # Test invalid update with float (should require Decimal)
    try:
        ds.price = 150.75
        print(f"Updated DStock price: {ds.price}")
    except Exception as e:
        print(f"Error updating DStock price: {e}")

    # Test valid update with Decimal
    try:
        ds.price = Decimal('155.25')
        print(f"Updated DStock price: {ds.price}, Cost: {ds.cost}")
    except Exception as e:
        print(f"Error updating DStock price: {e}")
    ```

6.  테스트 스크립트를 실행합니다.

    ```bash
    python /home/labex/project/test_subclass.py
    ```

    기본 `Stock` 클래스는 가격에 대해 float 값을 허용하고, `DStock` 서브클래스는 `Decimal` 값을 요구하는 것을 볼 수 있습니다.

    ```plaintext
    Stock: GOOG, Shares: 100, Price: 490.1, Cost: 49010.0
    Updated Stock price: 500.25, Cost: 50025.0
    DStock: AAPL, Shares: 50, Price: 142.50, Cost: 7125.00
    Error updating DStock price: Expected Decimal
    Updated DStock price: 155.25, Cost: 7762.50
    ```

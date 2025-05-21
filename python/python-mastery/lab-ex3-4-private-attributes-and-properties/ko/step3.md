# Property 유효성 검사 구현하기

Property 를 사용하면 속성 값을 가져오고, 설정하고, 삭제하는 방식을 제어할 수도 있습니다. 이는 속성에 유효성 검사를 추가하여 값이 특정 기준을 충족하는지 확인하는 데 유용합니다.

`Stock` 클래스에서 `shares`가 음수가 아닌 정수이고 `price`가 음수가 아닌 float 인지 확인하려고 합니다. 이를 위해 getter 와 setter 와 함께 property 데코레이터를 사용합니다.

**지침:**

1.  에디터에서 `stock.py` 파일을 엽니다.

2.  private 속성 `_shares` 및 `_price`를 `Stock` 클래스에 추가하고 생성자를 수정하여 사용합니다.

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares  # Using private attribute
        self._price = price    # Using private attribute
    ```

3.  유효성 검사가 있는 `shares` 및 `price`에 대한 property 를 정의합니다.

    ```python
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected integer")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Expected float")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value
    ```

4.  유효성 검사를 위해 property setter 를 사용하도록 생성자를 업데이트합니다.

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares  # Using property setter
        self.price = price    # Using property setter
    ```

5.  `stock.py` 파일을 저장합니다.

6.  `test_validation.py`라는 테스트 스크립트를 만듭니다.

    ```bash
    touch /home/labex/project/test_validation.py
    ```

7.  `test_validation.py` 파일에 다음 코드를 추가합니다.

    ```python
    from stock import Stock

    # Create a valid stock instance
    s = Stock('GOOG', 100, 490.10)
    print(f"Initial: Name={s.name}, Shares={s.shares}, Price={s.price}, Cost={s.cost}")

    # Test valid updates
    try:
        s.shares = 50  # Valid update
        print(f"After setting shares=50: Shares={s.shares}, Cost={s.cost}")
    except Exception as e:
        print(f"Error setting shares=50: {e}")

    try:
        s.price = 123.45  # Valid update
        print(f"After setting price=123.45: Price={s.price}, Cost={s.cost}")
    except Exception as e:
        print(f"Error setting price=123.45: {e}")

    # Test invalid updates
    try:
        s.shares = "50"  # Invalid type (string)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting shares='50': {e}")

    try:
        s.shares = -10  # Invalid value (negative)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting shares=-10: {e}")

    try:
        s.price = "123.45"  # Invalid type (string)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting price='123.45': {e}")

    try:
        s.price = -10.0  # Invalid value (negative)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting price=-10.0: {e}")
    ```

8.  테스트 스크립트를 실행합니다.

    ```bash
    python /home/labex/project/test_validation.py
    ```

    유효한 업데이트가 성공적으로 수행되고 유효하지 않은 업데이트에 대한 적절한 오류 메시지가 표시되는 출력을 볼 수 있습니다.

    ```plaintext
    Initial: Name=GOOG, Shares=100, Price=490.1, Cost=49010.0
    After setting shares=50: Shares=50, Cost=24505.0
    After setting price=123.45: Price=123.45, Cost=6172.5
    Error setting shares='50': Expected integer
    Error setting shares=-10: shares must be >= 0
    Error setting price='123.45': Expected float
    Error setting price=-10.0: price must be >= 0
    ```

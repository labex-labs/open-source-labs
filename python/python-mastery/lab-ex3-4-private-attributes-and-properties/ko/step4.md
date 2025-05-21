# 메모리 최적화를 위해 `__slots__` 사용하기

`__slots__` 속성은 클래스가 가질 수 있는 속성을 제한합니다. 이는 인스턴스에 새 속성을 추가하는 것을 방지하고 메모리 사용량을 줄입니다.

`Stock` 클래스에서 `__slots__`를 사용하여 다음을 수행합니다.

1.  속성 생성을 정의된 속성으로만 제한합니다.
2.  특히 많은 인스턴스를 생성할 때 메모리 효율성을 향상시킵니다.

**지침:**

1.  에디터에서 `stock.py` 파일을 엽니다.
2.  클래스에서 사용되는 모든 private 속성 이름을 나열하는 `__slots__` 클래스 변수를 추가합니다.

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Define slots to restrict attribute creation
        __slots__ = ('name', '_shares', '_price')

        # Rest of the class...
    ```

3.  파일을 저장합니다.

4.  `test_slots.py`라는 테스트 스크립트를 만듭니다.

    ```bash
    touch /home/labex/project/test_slots.py
    ```

5.  `test_slots.py` 파일에 다음 코드를 추가합니다.

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access existing attributes
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")

    # Try to add a new attribute
    try:
        s.extra = "This will fail"
        print(f"Extra: {s.extra}")
    except AttributeError as e:
        print(f"Error: {e}")
    ```

6.  테스트 스크립트를 실행합니다.

    ```bash
    python /home/labex/project/test_slots.py
    ```

    정의된 속성에 접근할 수 있지만 새 속성을 추가하려고 하면 `AttributeError`가 발생하는 것을 보여주는 출력을 볼 수 있습니다.

    ```plaintext
    Name: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    Error: 'Stock' object has no attribute 'extra'
    ```

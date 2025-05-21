# Private 속성 구현하기

Python 에서는 속성이 클래스 내에서 내부적으로 사용될 것임을 나타내기 위해 명명 규칙을 사용합니다. 이러한 속성 앞에 밑줄 (`_`) 을 붙입니다. 이는 다른 개발자에게 이러한 속성이 public API 의 일부가 아니며 클래스 외부에서 직접 접근해서는 안 된다는 것을 알립니다.

`stock.py` 파일에서 현재 `Stock` 클래스를 살펴보겠습니다. `types`라는 클래스 변수가 있습니다.

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

`types` 클래스 변수는 행 데이터를 변환하는 데 내부적으로 사용됩니다. 이것이 구현 세부 사항임을 나타내기 위해 private 로 표시하겠습니다.

**지침:**

1.  에디터에서 `stock.py` 파일을 엽니다.

2.  선행 밑줄을 추가하여 `types` 클래스 변수를 수정하여 `_types`로 변경합니다.

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Rest of the class...
    ```

3.  이름이 변경된 변수 `_types`를 사용하도록 `from_row` 메서드를 업데이트합니다.

    ```python
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    ```

4.  `stock.py` 파일을 저장합니다.

5.  변경 사항을 테스트하기 위해 `test_stock.py`라는 Python 스크립트를 만듭니다. 다음 명령을 사용하여 에디터에서 파일을 만들 수 있습니다.

    ```bash
    touch /home/labex/project/test_stock.py
    ```

6.  `test_stock.py` 파일에 다음 코드를 추가합니다. 이 코드는 `Stock` 클래스의 인스턴스를 생성하고 이에 대한 정보를 출력합니다.

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)
    print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
    print(f"Cost: {s.cost()}")

    # Create from row
    row = ['AAPL', '50', '142.5']
    apple = Stock.from_row(row)
    print(f"Name: {apple.name}, Shares: {apple.shares}, Price: {apple.price}")
    print(f"Cost: {apple.cost()}")
    ```

7.  터미널에서 다음 명령을 사용하여 테스트 스크립트를 실행합니다.

    ```bash
    python /home/labex/project/test_stock.py
    ```

    다음과 유사한 출력을 볼 수 있습니다.

    ```
    Name: GOOG, Shares: 100, Price: 490.1
    Cost: 49010.0
    Name: AAPL, Shares: 50, Price: 142.5
    Cost: 7125.0
    ```

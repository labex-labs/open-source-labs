# 클래스 메서드를 사용하여 대체 생성자 구현하기

이 단계에서는 클래스 메서드를 사용하여 대체 생성자를 구현하는 방법을 배우게 됩니다. 이를 통해 CSV 행 데이터에서 `Stock` 객체를 보다 우아한 방식으로 생성할 수 있습니다.

## 대체 생성자란 무엇인가요?

Python 에서 대체 생성자는 유용한 패턴입니다. 일반적으로 표준 `__init__` 메서드를 사용하여 객체를 생성합니다. 그러나 대체 생성자는 객체를 생성하는 추가적인 방법을 제공합니다. 클래스 메서드는 클래스 자체에 액세스할 수 있으므로 대체 생성자를 구현하는 데 매우 적합합니다.

## from_row() 클래스 메서드 구현하기

`Stock` 클래스에 클래스 변수 `types`와 클래스 메서드 `from_row()`를 추가합니다. 이렇게 하면 CSV 데이터에서 `Stock` 인스턴스를 생성하는 프로세스가 단순화됩니다.

강조 표시된 코드를 추가하여 `stock.py` 파일을 수정해 보겠습니다.

```python
# stock.py

class Stock:
    types = (str, int, float)  # Type conversions to apply to CSV data

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    @classmethod
    def from_row(cls, row):
        """
        Create a Stock instance from a row of CSV data.

        Args:
            row: A list of strings [name, shares, price]

        Returns:
            A new Stock instance
        """
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

# The rest of the file remains unchanged
```

이제 이 코드에서 무슨 일이 일어나는지 단계별로 이해해 보겠습니다.

1. 클래스 변수 `types`를 정의했습니다. 이는 유형 변환 함수 `(str, int, float)`를 포함하는 튜플입니다. 이러한 함수는 CSV 행의 데이터를 적절한 유형으로 변환하는 데 사용됩니다.
2. 클래스 메서드 `from_row()`를 추가했습니다. `@classmethod` 데코레이터는 이 메서드를 클래스 메서드로 표시합니다.
3. 이 메서드의 첫 번째 매개변수는 클래스 자체에 대한 참조인 `cls`입니다. 일반 메서드에서는 클래스의 인스턴스를 참조하기 위해 `self`를 사용하지만, 여기서는 클래스 메서드이므로 `cls`를 사용합니다.
4. `zip()` 함수는 `types`의 각 유형 변환 함수를 `row` 목록의 해당 값과 쌍으로 연결하는 데 사용됩니다.
5. 리스트 컴프리헨션을 사용하여 각 변환 함수를 `row` 목록의 해당 값에 적용합니다. 이렇게 하면 CSV 행의 문자열 데이터를 적절한 유형으로 변환합니다.
6. 마지막으로, 변환된 값을 사용하여 `Stock` 클래스의 새 인스턴스를 생성하고 반환합니다.

## 대체 생성자 테스트하기

이제 새 클래스 메서드를 테스트하기 위해 `test_class_method.py`라는 새 파일을 만들 것입니다. 이를 통해 대체 생성자가 예상대로 작동하는지 확인할 수 있습니다.

```python
# test_class_method.py
from stock import Stock

# Test the from_row() class method
row = ['AA', '100', '32.20']
s = Stock.from_row(row)

print(f"Stock: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost()}")

# Try with a different row
row2 = ['GOOG', '50', '1120.50']
s2 = Stock.from_row(row2)

print(f"\nStock: {s2.name}")
print(f"Shares: {s2.shares}")
print(f"Price: {s2.price}")
print(f"Cost: {s2.cost()}")
```

결과를 보려면 터미널에서 다음 명령을 실행하십시오.

```bash
cd ~/project
python test_class_method.py
```

다음과 유사한 출력이 표시되어야 합니다.

```
Stock: AA
Shares: 100
Price: 32.2
Cost: 3220.0

Stock: GOOG
Shares: 50
Price: 1120.5
Cost: 56025.0
```

이제 클래스 외부에서 수동으로 유형 변환을 수행하지 않고도 문자열 데이터에서 직접 `Stock` 인스턴스를 생성할 수 있습니다. 이렇게 하면 코드가 더 깔끔해지고 데이터 변환에 대한 책임이 클래스 자체 내에서 처리됩니다.

# 메서드를 Property 로 변환하기

Python 의 Property 를 사용하면 속성처럼 계산된 값에 접근할 수 있습니다. 이렇게 하면 메서드를 호출할 때 괄호가 필요 없어 코드가 더 깔끔하고 일관성이 있습니다.

현재 `Stock` 클래스에는 주식의 총 비용을 계산하는 `cost()` 메서드가 있습니다.

```python
def cost(self):
    return self.shares * self.price
```

비용 값을 얻으려면 괄호와 함께 호출해야 합니다.

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

`cost()` 메서드를 property 로 변환하여 괄호 없이 비용 값에 접근할 수 있도록 개선할 수 있습니다.

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

**지침:**

1.  에디터에서 `stock.py` 파일을 엽니다.

2.  `@property` 데코레이터를 사용하여 `cost()` 메서드를 property 로 바꿉니다.

    ```python
    @property
    def cost(self):
        return self.shares * self.price
    ```

3.  `stock.py` 파일을 저장합니다.

4.  에디터에서 `test_property.py`라는 새 파일을 만듭니다.

    ```bash
    touch /home/labex/project/test_property.py
    ```

5.  `test_property.py` 파일에 다음 코드를 추가하여 `Stock` 인스턴스를 생성하고 `cost` property 에 접근합니다.

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access cost as a property (no parentheses)
    print(f"Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")  # Using the property
    ```

6.  테스트 스크립트를 실행합니다.

    ```bash
    python /home/labex/project/test_property.py
    ```

    다음과 유사한 출력을 볼 수 있습니다.

    ```
    Stock: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    ```

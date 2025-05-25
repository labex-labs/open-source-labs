# 단순 속성 (Simple Attributes)

다음 클래스를 고려해 보세요.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

놀라운 특징은 속성을 어떤 값으로든 설정할 수 있다는 것입니다.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares = 100
>>> s.shares = "hundred"
>>> s.shares = [1, 0, 0]
>>>
```

이것을 보고 몇 가지 추가적인 검사를 원한다고 생각할 수 있습니다.

```python
s.shares = '50'     # Raise a TypeError, this is a string
```

어떻게 하시겠습니까?

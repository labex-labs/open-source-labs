# 딕셔너리와 객체

사용자 정의 객체 또한 인스턴스 데이터와 클래스 모두에 딕셔너리를 사용합니다. 사실, 전체 객체 시스템은 대부분 딕셔너리 위에 추가된 레이어입니다.

딕셔너리는 인스턴스 데이터, `__dict__`를 저장합니다.

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{'name' : 'GOOG', 'shares' : 100, 'price': 490.1 }
```

`self`에 할당할 때 이 딕셔너리 (및 인스턴스) 를 채웁니다.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

인스턴스 데이터, `self.__dict__`는 다음과 같습니다.

```python
{
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}
```

**각 인스턴스는 자체적인 개인 딕셔너리를 갖습니다.**

```python
s = Stock('GOOG', 100, 490.1)     # {'name' : 'GOOG','shares' : 100, 'price': 490.1 }
t = Stock('AAPL', 50, 123.45)     # {'name' : 'AAPL','shares' : 50, 'price': 123.45 }
```

어떤 클래스의 인스턴스를 100 개 생성했다면, 데이터를 저장하는 100 개의 딕셔너리가 존재합니다.

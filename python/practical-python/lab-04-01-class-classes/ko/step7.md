# 연습 문제 4.1: 데이터를 구조체로 사용하기 (Objects as Data Structures)

2 절과 3 절에서 우리는 튜플과 딕셔너리로 표현된 데이터를 사용했습니다. 예를 들어, 주식 보유는 다음과 같은 튜플로 표현될 수 있습니다.

```python
s = ('GOOG',100,490.10)
```

또는 다음과 같은 딕셔너리로 표현될 수 있습니다.

```python
s = { 'name'   : 'GOOG',
      'shares' : 100,
      'price'  : 490.10
}
```

이러한 데이터를 조작하기 위한 함수를 작성할 수도 있습니다. 예를 들어:

```python
def cost(s):
    return s['shares'] * s['price']
```

하지만 프로그램이 커지면 더 나은 조직감을 만들고 싶을 수 있습니다. 따라서 데이터를 표현하는 또 다른 방법은 클래스를 정의하는 것입니다. `stock.py`라는 파일을 만들고 단일 주식 보유를 나타내는 `Stock` 클래스를 정의합니다. `Stock`의 인스턴스가 `name`, `shares`, `price` 속성을 갖도록 합니다. 예를 들어:

```python
>>> import stock
>>> a = stock.Stock('GOOG',100,490.10)
>>> a.name
'GOOG'
>>> a.shares
100
>>> a.price
490.1
>>>
```

몇 개의 `Stock` 객체를 더 만들고 조작합니다. 예를 들어:

```python
>>> b = stock.Stock('AAPL', 50, 122.34)
>>> c = stock.Stock('IBM', 75, 91.75)
>>> b.shares * b.price
6117.0
>>> c.shares * c.price
6881.25
>>> stocks = [a, b, c]
>>> stocks
[<stock.Stock object at 0x37d0b0>, <stock.Stock object at 0x37d110>, <stock.Stock object at 0x37d050>]
>>> for s in stocks:
     print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')

... 출력을 확인하세요 ...
>>>
```

여기서 강조할 한 가지는 `Stock` 클래스가 객체의 인스턴스를 생성하는 팩토리처럼 작동한다는 것입니다. 기본적으로 함수처럼 호출하면 새로운 객체를 생성합니다. 또한 각 객체는 고유하다는 점을 강조해야 합니다. 즉, 각 객체는 생성된 다른 객체와 별개인 자체 데이터를 가지고 있습니다.

클래스에 의해 정의된 객체는 딕셔너리와 다소 유사합니다. 단지 약간 다른 구문을 사용합니다. 예를 들어, `s['name']` 또는 `s['price']`를 쓰는 대신, 이제 `s.name`과 `s.price`를 씁니다.

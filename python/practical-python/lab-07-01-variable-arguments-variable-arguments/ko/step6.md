# 연습 문제 7.2: 튜플 (tuple) 과 딕셔너리 (dict) 를 인자로 전달하기

파일에서 데이터를 읽어 다음과 같은 튜플을 얻었다고 가정해 봅시다:

```python
>>> data = ('GOOG', 100, 490.1)
>>>
```

이제 이 데이터를 사용하여 `Stock` 객체를 생성하고 싶다고 가정해 봅시다. `data`를 직접 전달하려고 하면 작동하지 않습니다:

```python
>>> from stock import Stock
>>> s = Stock(data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Stock.__init__() missing 2 required positional arguments: 'shares' and 'price'
>>>
```

이것은 대신 `*data`를 사용하여 쉽게 해결할 수 있습니다. 다음을 시도해 보세요:

```python
>>> s = Stock(*data)
>>> s
Stock('GOOG', 100, 490.1)
>>>
```

딕셔너리가 있는 경우, 대신 `**`를 사용할 수 있습니다. 예를 들어:

```python
>>> data = { 'name': 'GOOG', 'shares': 100, 'price': 490.1 }
>>> s = Stock(**data)
Stock('GOOG', 100, 490.1)
>>>
```

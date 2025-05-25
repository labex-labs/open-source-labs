# 연습 문제 5.5: 상속 (Inheritance)

`Stock`에서 상속하는 새 클래스를 만듭니다.

```python
>>> class NewStock(Stock):
        def yow(self):
            print('Yow!')

>>> n = NewStock('ACME', 50, 123.45)
>>> n.cost()
6172.50
>>> n.yow()
Yow!
>>>
```

상속은 속성에 대한 검색 프로세스를 확장하여 구현됩니다. `__bases__` 속성은 즉시 상위 클래스의 튜플을 갖습니다.

```python
>>> NewStock.__bases__
(<class 'stock.Stock'>,)
>>>
```

`__mro__` 속성은 속성을 검색할 순서대로 모든 상위 클래스의 튜플을 갖습니다.

```python
>>> NewStock.__mro__
(<class '__main__.NewStock'>, <class 'stock.Stock'>, <class 'object'>)
>>>
```

다음은 위의 인스턴스 `n`의 `cost()` 메서드를 찾는 방법입니다.

```python
>>> for cls in n.__class__.__mro__:
        if 'cost' in cls.__dict__:
            break

>>> cls
<class '__main__.Stock'>
>>> cls.__dict__['cost']
<function cost at 0x101aed598>
>>>
```

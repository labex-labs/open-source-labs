# 연습 문제 2.3: 몇 가지 추가적인 딕셔너리 연산

딕셔너리를 리스트로 변환하면 모든 키를 얻을 수 있습니다.

```python
>>> list(d)
['name', 'shares', 'price', 'date', 'account']
>>>
```

마찬가지로, `for` 문을 사용하여 딕셔너리를 반복하면 키를 얻게 됩니다.

```python
>>> for k in d:
        print('k =', k)

k = name
k = shares
k = price
k = date
k = account
>>>
```

동시에 조회를 수행하는 이 변형을 시도해 보십시오.

```python
>>> for k in d:
        print(k, '=', d[k])

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
account = 12345
>>>
```

`keys()` 메서드를 사용하여 모든 키를 얻을 수도 있습니다.

```python
>>> keys = d.keys()
>>> keys
dict_keys(['name', 'shares', 'price', 'date', 'account'])
>>>
```

`keys()`는 특별한 `dict_keys` 객체를 반환한다는 점에서 약간 특이합니다.

이것은 원래 딕셔너리에 대한 오버레이로, 딕셔너리가 변경되더라도 항상 현재 키를 제공합니다. 예를 들어, 다음을 시도해 보십시오.

```python
>>> del d['account']
>>> keys
dict_keys(['name', 'shares', 'price', 'date'])
>>>
```

`d.keys()`를 다시 호출하지 않았음에도 불구하고 `keys`에서 `'account'`가 사라졌다는 점에 주의하십시오.

키와 값을 함께 사용하는 더 우아한 방법은 `items()` 메서드를 사용하는 것입니다. 이 메서드는 `(key, value)` 튜플을 제공합니다.

```python
>>> items = d.items()
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> for k, v in d.items():
        print(k, '=', v)

name = AA
shares = 75
price = 32.2
date = (6, 11, 2007)
>>>
```

`items`와 같은 튜플이 있는 경우 `dict()` 함수를 사용하여 딕셔너리를 만들 수 있습니다. 시도해 보십시오.

```python
>>> items
dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])
>>> d = dict(items)
>>> d
{'name': 'AA', 'shares': 75, 'price':32.2, 'date': (6, 11, 2007)}
>>>
```

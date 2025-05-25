# 연습 문제 2.2: 데이터 구조로서의 딕셔너리 (Dictionaries)

튜플의 대안은 대신 딕셔너리를 만드는 것입니다.

```python
>>> d = {
        'name' : row[0],
        'shares' : int(row[1]),
        'price'  : float(row[2])
    }
>>> d
{'name': 'AA', 'shares': 100, 'price': 32.2 }
>>>
```

이 보유 자산의 총 비용을 계산합니다.

```python
>>> cost = d['shares'] * d['price']
>>> cost
3220.0000000000005
>>>
```

위의 튜플을 포함하는 동일한 계산과 이 예제를 비교합니다. 주식 수를 75 로 변경합니다.

```python
>>> d['shares'] = 75
>>> d
{'name': 'AA', 'shares': 75, 'price': 32.2 }
>>>
```

튜플과 달리 딕셔너리는 자유롭게 수정할 수 있습니다. 몇 가지 속성을 추가합니다.

```python
>>> d['date'] = (6, 11, 2007)
>>> d['account'] = 12345
>>> d
{'name': 'AA', 'shares': 75, 'price':32.2, 'date': (6, 11, 2007), 'account': 12345}
>>>
```

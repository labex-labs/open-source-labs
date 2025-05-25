# 연습 문제 1.19: 리스트 요소 추출 및 재할당

몇 가지 조회를 시도해 보십시오:

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'DOA'
>>>
```

값을 하나 재할당해 보십시오:

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']
>>>
```

몇 개의 슬라이스를 가져오십시오:

```python
>>> symlist[0:3]
['HPQ', 'AAPL', 'AIG']
>>> symlist[-2:]
['DOA', 'GOOG']
>>>
```

빈 리스트를 생성하고 항목을 추가하십시오.

```python
>>> mysyms = []
>>> mysyms.append('GOOG')
>>> mysyms
['GOOG']
```

리스트의 일부를 다른 리스트에 재할당할 수 있습니다. 예를 들어:

```python
>>> symlist[-2:] = mysyms
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
>>>
```

이렇게 하면 왼쪽 (left-hand-side) 의 리스트 (`symlist`) 가 오른쪽 (right-hand-side) 의 (`mysyms`) 에 맞게 적절하게 크기가 조정됩니다. 예를 들어, 위의 예에서 `symlist`의 마지막 두 항목이 `mysyms` 리스트의 단일 항목으로 대체되었습니다.

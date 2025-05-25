# 연습 문제 1.22: 항목 추가, 삽입 및 삭제

`append()` 메서드를 사용하여 심볼 `'RHT'`를 `symlist`의 끝에 추가하십시오.

```python
>>> symlist.append('RHT') # append 'RHT'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

`insert()` 메서드를 사용하여 심볼 `'AA'`를 리스트의 두 번째 항목으로 삽입하십시오.

```python
>>> symlist.insert(1, 'AA') # Insert 'AA' as the second item in the list
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

`remove()` 메서드를 사용하여 리스트에서 `'MSFT'`를 제거하십시오.

```python
>>> symlist.remove('MSFT') # Remove 'MSFT'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
>>>
```

리스트의 끝에 `'YHOO'`의 중복 항목을 추가하십시오.

_참고: 리스트에 중복된 값이 있는 것은 괜찮습니다._

```python
>>> symlist.append('YHOO') # Append 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT', 'YHOO']
>>>
```

`index()` 메서드를 사용하여 리스트에서 `'YHOO'`의 첫 번째 위치를 찾으십시오.

```python
>>> symlist.index('YHOO') # Find the first index of 'YHOO'
4
>>> symlist[4]
'YHOO'
>>>
```

`'YHOO'`가 리스트에 몇 번 있는지 세어보십시오:

```python
>>> symlist.count('YHOO')
2
>>>
```

`'YHOO'`의 첫 번째 발생을 제거하십시오.

```python
>>> symlist.remove('YHOO') # Remove first occurrence 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'GOOG', 'RHT', 'YHOO']
>>>
```

참고로, 항목의 모든 발생을 찾거나 제거하는 메서드는 없습니다. 하지만 섹션 2 에서 이를 수행하는 우아한 방법을 볼 것입니다.

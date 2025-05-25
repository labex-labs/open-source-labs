# 연습 문제 1.23: 정렬 (Sorting)

리스트를 정렬하고 싶으십니까? `sort()` 메서드를 사용하십시오. 시도해 보십시오:

```python
>>> symlist.sort()
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']
>>>
```

역순으로 정렬하고 싶으십니까? 다음을 시도해 보십시오:

```python
>>> symlist.sort(reverse=True)
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>>
```

참고: 리스트를 정렬하면 내용이 '제자리에서' 수정됩니다. 즉, 리스트의 요소가 섞이지만 결과로 새로운 리스트가 생성되지 않습니다.

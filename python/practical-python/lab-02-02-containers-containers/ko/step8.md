# 세트 (Sets)

세트는 정렬되지 않은 고유 항목들의 모음입니다.

```python
tech_stocks = { 'IBM','AAPL','MSFT' }
# Alternative syntax
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])
```

세트는 멤버십 테스트 (membership tests) 에 유용합니다.

```python
>>> tech_stocks
set(['AAPL', 'IBM', 'MSFT'])
>>> 'IBM' in tech_stocks
True
>>> 'FB' in tech_stocks
False
>>>
```

세트는 중복 제거에도 유용합니다.

```python
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']

unique = set(names)
# unique = set(['IBM', 'AAPL','GOOG','YHOO'])
```

추가적인 세트 연산:

```python
unique.add('CAT')        # Add an item
unique.remove('YHOO')    # Remove an item

s1 = { 'a', 'b', 'c'}
s2 = { 'c', 'd' }
s1 | s2                 # Set union { 'a', 'b', 'c', 'd' }
s1 & s2                 # Set intersection { 'c' }
s1 - s2                 # Set difference { 'a', 'b' }
```

이 연습에서는 이 과정의 나머지 부분에서 사용될 주요 프로그램 중 하나를 구축하기 시작합니다. `report.py` 파일에서 작업을 수행하십시오.

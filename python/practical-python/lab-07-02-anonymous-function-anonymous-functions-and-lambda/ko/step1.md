# 리스트 정렬 재검토

리스트는 _in-place_ 방식으로 정렬될 수 있습니다. `sort` 메서드를 사용합니다.

```python
s = [10,1,7,3]
s.sort() # s = [1,3,7,10]
```

역순으로 정렬할 수 있습니다.

```python
s = [10,1,7,3]
s.sort(reverse=True) # s = [10,7,3,1]
```

아주 간단해 보입니다. 하지만, 딕셔너리 (dict) 의 리스트는 어떻게 정렬할까요?

```python
[{'name': 'AA', 'price': 32.2, 'shares': 100},
{'name': 'IBM', 'price': 91.1, 'shares': 50},
{'name': 'CAT', 'price': 83.44, 'shares': 150},
{'name': 'MSFT', 'price': 51.23, 'shares': 200},
{'name': 'GE', 'price': 40.37, 'shares': 95},
{'name': 'MSFT', 'price': 65.1, 'shares': 50},
{'name': 'IBM', 'price': 70.44, 'shares': 100}]
```

어떤 기준에 따라 정렬할까요?

*key function*을 사용하여 정렬을 안내할 수 있습니다. *key function*은 딕셔너리를 받아 정렬에 필요한 값을 반환하는 함수입니다.

```python
portfolio = [
    {'name': 'AA', 'price': 32.2, 'shares': 100},
    {'name': 'IBM', 'price': 91.1, 'shares': 50},
    {'name': 'CAT', 'price': 83.44, 'shares': 150},
    {'name': 'MSFT', 'price': 51.23, 'shares': 200},
    {'name': 'GE', 'price': 40.37, 'shares': 95},
    {'name': 'MSFT', 'price': 65.1, 'shares': 50},
    {'name': 'IBM', 'price': 70.44, 'shares': 100}
]

def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)
```

결과는 다음과 같습니다.

```python
# Check how the dictionaries are sorted by the `name` key
[
  {'name': 'AA', 'price': 32.2, 'shares': 100},
  {'name': 'CAT', 'price': 83.44, 'shares': 150},
  {'name': 'GE', 'price': 40.37, 'shares': 95},
  {'name': 'IBM', 'price': 91.1, 'shares': 50},
  {'name': 'IBM', 'price': 70.44, 'shares': 100},
  {'name': 'MSFT', 'price': 51.23, 'shares': 200},
  {'name': 'MSFT', 'price': 65.1, 'shares': 50}
]
```

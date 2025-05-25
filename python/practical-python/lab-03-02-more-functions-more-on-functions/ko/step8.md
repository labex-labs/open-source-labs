# 지역 변수 (Local Variables)

함수 내에서 할당된 변수는 비공개 (private) 변수입니다.

```python
def read_portfolio(filename):
    portfolio = []
    for line in open(filename):
        fields = line.split(',')
        s = (fields[0], int(fields[1]), float(fields[2]))
        portfolio.append(s)
    return portfolio
```

이 예제에서 `filename`, `portfolio`, `line`, `fields` 및 `s`는 지역 변수입니다. 이러한 변수는 함수 호출 후 유지되거나 접근할 수 없습니다.

```python
>>> stocks = read_portfolio('portfolio.csv')
>>> fields
Traceback (most recent call last):
File "<stdin>", line 1, in ?
NameError: name 'fields' is not defined
>>>
```

지역 변수는 또한 다른 곳에서 발견된 변수와 충돌할 수 없습니다.

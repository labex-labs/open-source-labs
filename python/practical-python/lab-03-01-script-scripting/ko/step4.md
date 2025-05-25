# 함수 정의하기

단일 *작업 (task)*과 관련된 모든 코드를 한 곳에 두는 것이 좋습니다. 함수를 사용하십시오.

```python
def read_prices(filename):
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

함수는 반복적인 작업도 단순화합니다.

```python
oldprices = read_prices('oldprices.csv')
newprices = read_prices('newprices.csv')
```

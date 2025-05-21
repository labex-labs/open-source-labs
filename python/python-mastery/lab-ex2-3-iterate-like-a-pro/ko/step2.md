# `enumerate()` 및 `zip()` 함수 사용하기

이 단계에서는 반복에 필수적인 Python 의 두 가지 매우 유용한 내장 함수인 `enumerate()`와 `zip()`을 살펴보겠습니다. 이러한 함수는 시퀀스로 작업할 때 코드를 크게 단순화할 수 있습니다.

## `enumerate()`로 카운팅하기

시퀀스를 반복할 때 각 항목의 인덱스 또는 위치를 추적해야 하는 경우가 많습니다. 이때 `enumerate()` 함수가 유용합니다. `enumerate()` 함수는 시퀀스를 입력으로 받아 해당 시퀀스의 각 항목에 대해 (인덱스, 값) 쌍을 반환합니다.

이전 단계에서 Python 인터프리터를 따라 진행했다면 계속 사용할 수 있습니다. 그렇지 않은 경우 새 세션을 시작하십시오. 처음부터 시작하는 경우 데이터를 설정하는 방법은 다음과 같습니다.

```python
# If you're starting a new session, reload the data first:
# import csv
# f = open('portfolio.csv')
# f_csv = csv.reader(f)
# headers = next(f_csv)
# rows = list(f_csv)

# Use enumerate to get row numbers
for rowno, row in enumerate(rows):
    print(rowno, row)
```

위 코드를 실행하면 `enumerate(rows)` 함수는 인덱스 (0 부터 시작) 와 `rows` 시퀀스에서 해당 행의 쌍을 생성합니다. 그런 다음 `for` 루프는 이러한 쌍을 `rowno` 및 `row` 변수로 언패킹하고 이를 출력합니다.

출력:

```
0 ['AA', '100', '32.20']
1 ['IBM', '50', '91.10']
2 ['CAT', '150', '83.44']
3 ['MSFT', '200', '51.23']
4 ['GE', '95', '40.37']
5 ['MSFT', '50', '65.10']
6 ['IBM', '100', '70.44']
```

`enumerate()`를 언패킹과 결합하여 코드를 더욱 읽기 쉽게 만들 수 있습니다. 언패킹을 사용하면 시퀀스의 요소를 개별 변수에 직접 할당할 수 있습니다.

```python
for rowno, (name, shares, price) in enumerate(rows):
    print(rowno, name, shares, price)
```

이 코드에서는 `(name, shares, price)` 주위에 추가 괄호 쌍을 사용하여 행 데이터를 올바르게 언패킹하고 있습니다. `enumerate(rows)`는 여전히 인덱스와 행을 제공하지만, 이제 행을 `name`, `shares`, `price` 변수로 언패킹하고 있습니다.

출력:

```
0 AA 100 32.20
1 IBM 50 91.10
2 CAT 150 83.44
3 MSFT 200 51.23
4 GE 95 40.37
5 MSFT 50 65.10
6 IBM 100 70.44
```

## `zip()`으로 데이터 페어링하기

`zip()` 함수는 Python 의 또 다른 강력한 도구입니다. 여러 시퀀스의 해당 요소를 결합하는 데 사용됩니다. 여러 시퀀스를 `zip()`에 전달하면 각 튜플에 동일한 위치의 각 입력 시퀀스에서 가져온 요소가 포함된 튜플을 생성하는 반복자가 생성됩니다.

`headers` 및 `row` 데이터와 함께 `zip()`을 사용하는 방법을 살펴보겠습니다.

```python
# Recall the headers variable from earlier
print(headers)  # Should show ['name', 'shares', 'price']

# Get the first row
row = rows[0]
print(row)      # Should show ['AA', '100', '32.20']

# Use zip to pair column names with values
for col, val in zip(headers, row):
    print(col, val)
```

이 코드에서 `zip(headers, row)`는 `headers` 시퀀스와 `row` 시퀀스를 가져와 해당 요소를 페어링합니다. 그런 다음 `for` 루프는 이러한 쌍을 `col`(headers 의 열 이름) 과 `val`(row 의 값) 로 언패킹하고 이를 출력합니다.

출력:

```
['name', 'shares', 'price']
['AA', '100', '32.20']
name AA
shares 100
price 32.20
```

`zip()`의 매우 일반적인 사용 사례 중 하나는 키 - 값 쌍에서 딕셔너리를 만드는 것입니다. Python 에서 딕셔너리는 키 - 값 쌍의 모음입니다.

```python
# Create a dictionary from headers and row values
record = dict(zip(headers, row))
print(record)
```

여기서 `zip(headers, row)`는 열 이름과 값의 쌍을 생성하고 `dict()` 함수는 이러한 쌍을 가져와 딕셔너리로 변환합니다.

출력:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
```

이 아이디어를 확장하여 `rows` 시퀀스의 모든 행을 딕셔너리로 변환할 수 있습니다.

```python
# Convert all rows to dictionaries
for row in rows:
    record = dict(zip(headers, row))
    print(record)
```

이 루프에서 `rows`의 각 행에 대해 `zip(headers, row)`를 사용하여 키 - 값 쌍을 생성한 다음 `dict()`를 사용하여 해당 쌍을 딕셔너리로 변환합니다. 이 기술은 데이터 처리 애플리케이션, 특히 첫 번째 행에 헤더가 포함된 CSV 파일로 작업할 때 매우 일반적입니다.

출력:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'IBM', 'shares': '50', 'price': '91.10'}
{'name': 'CAT', 'shares': '150', 'price': '83.44'}
{'name': 'MSFT', 'shares': '200', 'price': '51.23'}
{'name': 'GE', 'shares': '95', 'price': '40.37'}
{'name': 'MSFT', 'shares': '50', 'price': '65.10'}
{'name': 'IBM', 'shares': '100', 'price': '70.44'}
```

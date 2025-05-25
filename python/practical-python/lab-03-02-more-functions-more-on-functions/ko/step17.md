# 연습 3.7: 다른 열 구분 기호 선택

CSV 파일은 매우 일반적이지만, 탭이나 공백과 같은 다른 열 구분 기호를 사용하는 파일을 만날 수도 있습니다. 예를 들어, `portfolio.dat` 파일은 다음과 같습니다.

```csv
name shares price
"AA" 100 32.20
"IBM" 50 91.10
"CAT" 150 83.44
"MSFT" 200 51.23
"GE" 95 40.37
"MSFT" 50 65.10
"IBM" 100 70.44
```

`csv.reader()` 함수는 다음과 같이 다른 열 구분 기호를 제공할 수 있습니다.

```python
rows = csv.reader(f, delimiter=' ')
```

`/home/labex/project/fileparse_3.7.py`의 `parse_csv()` 함수를 수정하여 구분 기호를 변경할 수 있도록 합니다.

예를 들어:

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.dat', types=[str, int, float], delimiter=' ')
>>> portfolio
[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}, {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>>
```

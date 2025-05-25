# 연습 문제 2.16: zip() 함수 사용하기

`portfolio.csv` 파일의 첫 번째 줄에는 열 머리글 (column headers) 이 포함되어 있습니다. 이전의 모든 코드에서 우리는 그것들을 버렸습니다.

```python
>>> f = open('/home/labex/project/portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'shares', 'price']
>>>
```

하지만, 머리글을 유용하게 사용할 수 있다면 어떨까요? 이것이 `zip()` 함수가 등장하는 부분입니다. 먼저 파일 머리글을 데이터 행과 쌍으로 묶어보세요.

```python
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> list(zip(headers, row))
[ ('name', 'AA'), ('shares', '100'), ('price', '32.20') ]
>>>
```

`zip()`이 열 머리글을 열 값과 어떻게 쌍으로 묶었는지 확인하세요. 여기서는 결과를 볼 수 있도록 `list()`를 사용하여 리스트로 변환했습니다. 일반적으로 `zip()`은 for 루프에 의해 소비되어야 하는 이터레이터 (iterator) 를 생성합니다.

이 쌍으로 묶는 것은 딕셔너리 (dictionary) 를 구축하기 위한 중간 단계입니다. 이제 다음을 시도해 보세요.

```python
>>> record = dict(zip(headers, row))
>>> record
{'price': '32.20', 'name': 'AA', 'shares': '100'}
>>>
```

이 변환은 많은 데이터 파일을 처리할 때 알아두면 가장 유용한 트릭 중 하나입니다. 예를 들어, `pcost.py` 프로그램이 다양한 입력 파일에서 작동하도록 하되, 이름, 주식 수, 가격이 나타나는 실제 열 번호는 고려하지 않으려는 경우를 생각해 보세요.

`pcost.py`의 `portfolio_cost()` 함수를 다음과 같이 수정하세요.

```python
# pcost.py

def portfolio_cost(filename):
    ...
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
        ...
```

이제 완전히 다른 데이터 파일 `portfoliodate.csv`에서 함수를 시도해 보세요. 이 파일은 다음과 같습니다.

```csv
name,date,time,shares,price
"AA","6/11/2007","9:50am",100,32.20
"IBM","5/13/2007","4:20pm",50,91.10
"CAT","9/23/2006","1:30pm",150,83.44
"MSFT","5/17/2007","10:30am",200,51.23
"GE","2/1/2006","10:45am",95,40.37
"MSFT","10/31/2006","12:05pm",50,65.10
"IBM","7/9/2006","3:15pm",100,70.44
```

```python
>>> portfolio_cost('/home/labex/project/portfoliodate.csv')
44671.15
>>>
```

제대로 했다면, 데이터 파일이 이전과 완전히 다른 열 형식을 가지고 있음에도 불구하고 프로그램이 여전히 작동하는 것을 알 수 있을 것입니다. 멋지죠!

여기서 이루어진 변경은 미묘하지만 중요합니다. `portfolio_cost()`가 단일 고정 파일 형식을 읽도록 하드코딩 (hardcoded) 하는 대신, 새 버전은 모든 CSV 파일을 읽고 관심 있는 값을 선택합니다. 파일에 필요한 열이 있는 한 코드는 작동합니다.

섹션 2.3 에서 작성한 `report.py` 프로그램을 수정하여 동일한 기술을 사용하여 열 머리글을 선택하도록 하세요.

`portfoliodate.csv` 파일에서 `report.py` 프로그램을 실행하여 이전과 동일한 답을 생성하는지 확인하세요.

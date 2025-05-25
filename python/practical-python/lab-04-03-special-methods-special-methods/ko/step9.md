# 연습 문제 4.10: `getattr()` 사용 예시

`getattr()`는 속성을 읽는 대체 메커니즘입니다. 이것은 매우 유연한 코드를 작성하는 데 사용될 수 있습니다. 시작하려면 다음 예제를 시도해 보십시오:

```python
>>> import stock
>>> s = stock.Stock('GOOG', 100, 490.1)
>>> columns = ['name', 'shares']
>>> for colname in columns:
        print(colname, '=', getattr(s, colname))

name = GOOG
shares = 100
>>>
```

출력 데이터가 `columns` 변수에 나열된 속성 이름에 의해 완전히 결정된다는 점을 주의 깊게 관찰하십시오.

`tableformat.py` 파일에서 이 아이디어를 가져와 임의 객체 목록의 사용자 지정 속성을 표시하는 테이블을 인쇄하는 일반화된 함수 `print_table()`로 확장합니다. 이전의 `print_report()` 함수와 마찬가지로, `print_table()`도 출력 형식을 제어하기 위해 `TableFormatter` 인스턴스를 허용해야 합니다. 작동 방식은 다음과 같습니다:

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('txt')
>>> print_table(portfolio, ['name','shares'], formatter)
      name     shares
---------- ----------
        AA        100
       IBM         50
       CAT        150
      MSFT        200
        GE         95
      MSFT         50
       IBM        100

>>> print_table(portfolio, ['name','shares','price'], formatter)
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

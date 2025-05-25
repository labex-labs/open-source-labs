# 연습 문제 2.15: 실용적인 enumerate() 예제

`missing.csv` 파일에는 주식 포트폴리오 (stock portfolio) 데이터가 포함되어 있지만, 일부 행에 데이터가 누락되어 있다는 것을 기억하세요. `enumerate()`를 사용하여, 잘못된 입력을 발견할 때 경고 메시지와 함께 행 번호를 출력하도록 `pcost.py` 프로그램을 수정하세요.

```python
>>> cost = portfolio_cost('/home/labex/project/missing.csv')
Row 4: Couldn't convert: ['MSFT', '', '51.23']
Row 7: Couldn't convert: ['IBM', '', '70.44']
>>>
```

이렇게 하려면 코드의 몇 부분을 변경해야 합니다.

```python
...
for rowno, row in enumerate(rows, start=1):
    try:
        ...
    except ValueError:
        print(f'Row {rowno}: Bad row: {row}')
```

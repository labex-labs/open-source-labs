# 연습 문제 4.4: 클래스 사용하기 (Using your class)

`report.py` 프로그램의 `read_portfolio()` 함수를 수정하여 연습 문제 4.3 에서 보여준 것처럼 포트폴리오를 `Stock` 인스턴스 목록으로 읽도록 합니다. 그런 다음 `report.py` 및 `pcost.py`의 모든 코드를 수정하여 딕셔너리 대신 `Stock` 인스턴스로 작동하도록 합니다.

힌트: 코드에 큰 변경을 할 필요는 없습니다. 주로 `s['shares']`와 같은 딕셔너리 접근을 `s.shares`로 변경하게 됩니다.

이전과 동일하게 함수를 실행할 수 있어야 합니다.

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```

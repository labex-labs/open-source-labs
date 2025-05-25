# 연습 문제 4.8: 모든 것을 통합하기

`report.py` 프로그램을 수정하여 `portfolio_report()` 함수가 출력 형식을 지정하는 선택적 인수를 받도록 합니다. 예를 들어:

```python
>>> report.portfolio_report('portfolio.csv', 'prices.csv', 'txt')
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

명령줄에서 형식을 지정할 수 있도록 주 프로그램을 수정합니다.

```bash
$ python3 report.py portfolio.csv prices.csv csv
Name,Shares,Price,Change
AA,100,9.22,-22.98
IBM,50,106.28,15.18
CAT,150,35.46,-47.98
MSFT,200,20.89,-30.34
GE,95,13.48,-26.89
MSFT,50,20.89,-44.21
IBM,100,106.28,35.84
$
```

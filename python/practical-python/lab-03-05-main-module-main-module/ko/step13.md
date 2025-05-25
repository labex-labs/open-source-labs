# 연습 문제 3.15: `main()` 함수

`report.py` 파일에 명령줄 옵션 목록을 받아 이전과 동일한 출력을 생성하는 `main()` 함수를 추가하십시오. 다음과 같이 대화형으로 실행할 수 있습니다.

```python
>>> import report
>>> report.main(['/home/labex/project/report.py', '/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv'])
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

`pcost.py` 파일을 수정하여 유사한 `main()` 함수를 갖도록 하십시오.

```python
>>> import pcost
>>> pcost.main(['/home/labex/project/pcost.py', '/home/labex/project/portfolio.csv'])
Total cost: 44671.15
>>>
```

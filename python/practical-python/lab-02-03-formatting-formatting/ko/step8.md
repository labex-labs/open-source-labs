# 연습 문제 2.10: 서식 지정된 표 출력

연습 문제 2.9 의 for-loop 를 다시 수행하되, print 문을 변경하여 튜플의 서식을 지정합니다.

```python
>>> for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

          AA        100       9.22     -22.98
         IBM         50     106.28      15.18
         CAT        150      35.46     -47.98
        MSFT        200      20.89     -30.34
...
>>>
```

값을 확장하고 f-string 을 사용할 수도 있습니다. 예를 들어:

```python
>>> for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

          AA        100       9.22     -22.98
         IBM         50     106.28      15.18
         CAT        150      35.46     -47.98
        MSFT        200      20.89     -30.34
...
>>>
```

위의 문을 가져와 `report.py` 프로그램에 추가하십시오. 프로그램이 `make_report()` 함수의 출력을 받아 표시된 것처럼 깔끔하게 서식이 지정된 표를 출력하도록 하십시오.

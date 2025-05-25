# 다중 상속 (Multiple Inheritance)

클래스 정의에서 여러 클래스를 지정하여 여러 클래스에서 상속받을 수 있습니다.

```python
class Mother:
    ...

class Father:
    ...

class Child(Mother, Father):
    ...
```

`Child` 클래스는 두 부모로부터 기능을 상속받습니다. 몇 가지 까다로운 세부 사항이 있습니다. 무엇을 하고 있는지 확실히 알고 있지 않다면 사용하지 마십시오. 다음 섹션에서 추가 정보가 제공되지만, 이 과정에서는 다중 상속을 더 이상 사용하지 않을 것입니다.

상속의 주요 용도는 특히 라이브러리나 프레임워크에서 다양한 방식으로 확장하거나 사용자 정의할 수 있도록 설계된 코드를 작성하는 것입니다. 예를 들어, `report.py` 프로그램의 `print_report()` 함수를 생각해 보십시오. 다음과 같은 형태일 것입니다.

```python
def print_report(reportdata):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)
```

보고서 프로그램을 실행하면 다음과 같은 출력을 얻을 수 있습니다.

```python
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
```

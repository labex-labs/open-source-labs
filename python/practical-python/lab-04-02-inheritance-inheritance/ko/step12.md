# 연습 문제 4.5: 확장성 문제

`print_report()` 함수를 수정하여 일반 텍스트, HTML, CSV 또는 XML 과 같은 다양한 출력 형식을 지원하려는 경우를 가정해 보겠습니다. 이를 위해 모든 것을 수행하는 거대한 함수 하나를 작성할 수 있습니다. 그러나 그렇게 하면 유지 관리가 불가능한 혼란을 초래할 수 있습니다. 대신, 이는 상속을 사용하는 완벽한 기회입니다.

시작하려면 테이블을 만드는 데 관련된 단계에 집중하십시오. 테이블 상단에는 테이블 헤더 집합이 있습니다. 그 후, 테이블 데이터 행이 나타납니다. 이러한 단계를 가져와 자체 클래스에 넣습니다. `tableformat.py`라는 파일을 만들고 다음 클래스를 정의합니다.

```python
# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()
```

이 클래스는 아무것도 하지 않지만, 곧 정의될 추가 클래스에 대한 일종의 설계 사양 역할을 합니다. 이와 같은 클래스를 때때로 "추상 기본 클래스 (abstract base class)"라고 합니다.

`print_report()` 함수를 수정하여 `TableFormatter` 객체를 입력으로 받아 출력을 생성하기 위해 해당 객체에서 메서드를 호출하도록 합니다. 예를 들어, 다음과 같이 합니다.

```python
# report.py
...

def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)
```

`print_report()`에 인수를 추가했으므로 `portfolio_report()` 함수도 수정해야 합니다. 다음과 같이 `TableFormatter`를 생성하도록 변경합니다.

```python
# report.py

import tableformat

...
def portfolio_report(portfoliofile, pricefile):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.TableFormatter()
    print_report(report, formatter)
```

이 새로운 코드를 실행합니다.

```python
>>> ================================ RESTART ================================
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... crashes ...
```

`NotImplementedError` 예외로 즉시 충돌해야 합니다. 그렇게 흥미롭지는 않지만, 정확히 예상했던 것입니다. 다음 부분으로 진행합니다.

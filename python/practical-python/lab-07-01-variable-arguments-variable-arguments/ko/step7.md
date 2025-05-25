# 연습 문제 7.3: 인스턴스 (instance) 목록 생성하기

`report.py` 프로그램에서 다음과 같은 코드를 사용하여 인스턴스 목록을 생성했습니다:

```python
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                               select=['name','shares','price'],
                               types=[str,int,float])

    portfolio = [ Stock(d['name'], d['shares'], d['price'])
                  for d in portdicts ]
    return Portfolio(portfolio)
```

`Stock(**d)`를 대신 사용하여 해당 코드를 단순화할 수 있습니다. 변경해 보세요.

# 연습 문제 4.3: 인스턴스 목록 만들기 (Creating a list of instances)

딕셔너리 목록에서 `Stock` 인스턴스 목록을 만들려면 다음 단계를 시도해 보세요. 그런 다음 총 비용을 계산합니다.

```python
>>> import fileparse
>>> with open('portfolio.csv') as lines:
...     portdicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
...
>>> portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
>>> portfolio
[<stock.Stock object at 0x10c9e2128>, <stock.Stock object at 0x10c9e2048>, <stock.Stock object at 0x10c9e2080>,
 <stock.Stock object at 0x10c9e25f8>, <stock.Stock object at 0x10c9e2630>, <stock.Stock object at 0x10ca6f748>,
 <stock.Stock object at 0x10ca6f7b8>]
>>> sum([s.cost() for s in portfolio])
44671.15
>>>
```

# 연습 문제 7.4: 인자 (argument) 전달

`fileparse.parse_csv()` 함수는 파일 구분 기호 변경 및 오류 보고를 위한 몇 가지 옵션을 가지고 있습니다. 아마도 위에서 언급한 `read_portfolio()` 함수에 이러한 옵션을 노출하고 싶을 것입니다. 다음과 같이 변경하세요:

    def read_portfolio(filename, **opts):
        '''
        Read a stock portfolio file into a list of dictionaries with keys
        name, shares, and price.
        '''
        with open(filename) as lines:
            portdicts = fileparse.parse_csv(lines,
                                            select=['name','shares','price'],
                                            types=[str,int,float],
                                            **opts)

        portfolio = [ Stock(**d) for d in portdicts ]
        return Portfolio(portfolio)

변경을 완료한 후, 몇 가지 오류가 있는 파일을 읽어보세요:

```python
>>> import report
>>> port = report.read_portfolio('missing.csv')
Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
```

이제 오류를 숨겨보세요:

```python
>>> import report
>>> port = report.read_portfolio('missing.csv', silence_errors=True)
>>>
```

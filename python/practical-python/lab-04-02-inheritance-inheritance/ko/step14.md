# 연습 문제 4.7: 다형성 (Polymorphism) 실행

객체 지향 프로그래밍의 주요 특징은 객체를 프로그램에 연결하면 기존 코드를 변경하지 않고도 작동한다는 것입니다. 예를 들어, `TableFormatter` 객체를 사용하도록 예상하는 프로그램을 작성했다면, 실제로 어떤 종류의 `TableFormatter`를 제공하든 상관없이 작동합니다. 이러한 동작을 때때로 "다형성 (polymorphism)"이라고 합니다.

한 가지 잠재적인 문제는 사용자가 원하는 포맷터를 선택할 수 있도록 하는 방법을 파악하는 것입니다. `TextTableFormatter`와 같은 클래스 이름을 직접 사용하는 것은 종종 성가십니다. 따라서 몇 가지 단순화된 접근 방식을 고려할 수 있습니다. 아마도 다음과 같이 코드에 `if`-문을 포함할 수 있습니다.

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    if fmt == 'txt':
        formatter = tableformat.TextTableFormatter()
    elif fmt == 'csv':
        formatter = tableformat.CSVTableFormatter()
    elif fmt == 'html':
        formatter = tableformat.HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    print_report(report, formatter)
```

이 코드에서 사용자는 `'txt'` 또는 `'csv'`와 같은 단순화된 이름을 지정하여 형식을 선택합니다. 그러나 `portfolio_report()` 함수에 큰 `if`-문을 넣는 것이 최선의 아이디어일까요? 해당 코드를 다른 곳의 범용 함수로 이동하는 것이 더 나을 수 있습니다.

`tableformat.py` 파일에 사용자가 `'txt'`, `'csv'` 또는 `'html'`과 같은 출력 이름을 지정하여 포맷터를 생성할 수 있도록 하는 함수 `create_formatter(name)`을 추가합니다. `portfolio_report()`를 다음과 같이 수정합니다.

```python
def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
```

다양한 형식으로 함수를 호출하여 제대로 작동하는지 확인합니다.

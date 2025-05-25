# 람다 사용 (Using lambda)

- 람다는 매우 제한적입니다.
- 단일 표현식만 허용됩니다.
- `if`, `while` 등과 같은 문 (statement) 은 허용되지 않습니다.
- 가장 일반적인 사용 사례는 `sort()`와 같은 함수와 함께 사용됩니다.

일부 주식 포트폴리오 데이터를 읽고 이를 목록으로 변환합니다:

```python
>>> import report
>>> portfolio = list(report.read_portfolio('portfolio.csv'))
>>> for s in portfolio:
        print(s)

Stock('AA', 100, 32.2)
Stock('IBM', 50, 91.1)
Stock('CAT', 150, 83.44)
Stock('MSFT', 200, 51.23)
Stock('GE', 95, 40.37)
Stock('MSFT', 50, 65.1)
Stock('IBM', 100, 70.44)
>>>
```

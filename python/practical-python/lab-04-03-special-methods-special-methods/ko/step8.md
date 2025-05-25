# 연습 문제 4.9: 객체 출력을 위한 더 나은 출력

`stock.py`에서 정의한 `Stock` 객체를 수정하여 `__repr__()` 메서드가 더 유용한 출력을 생성하도록 합니다. 예를 들어:

```python
>>> goog = stock.Stock('GOOG', 100, 490.1)
>>> goog
Stock('GOOG', 100, 490.1)
>>>
```

이러한 변경을 한 후 주식 포트폴리오를 읽고 결과 목록을 볼 때 어떤 일이 발생하는지 확인하십시오. 예를 들어:

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> portfolio
... see what the output is ...
>>>
```

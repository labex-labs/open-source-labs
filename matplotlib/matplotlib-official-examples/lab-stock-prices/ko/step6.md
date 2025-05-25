# 겹침을 방지하기 위해 레이블 위치를 수직으로 수동 조정

```python
y_offsets = {k: 0 for k in stocks_ticker}
y_offsets['IBM'] = 5
y_offsets['AAPL'] = -5
y_offsets['AMZN'] = -6
```

# 垂直方向にラベルの位置を手動で調整して重複を回避する

```python
y_offsets = {k: 0 for k in stocks_ticker}
y_offsets['IBM'] = 5
y_offsets['AAPL'] = -5
y_offsets['AMZN'] = -6
```

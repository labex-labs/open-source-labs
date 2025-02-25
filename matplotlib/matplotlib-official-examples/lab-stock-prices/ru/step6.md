# Ручной подбор позиций меток по вертикали для избежания наложений

```python
y_offsets = {k: 0 for k in stocks_ticker}
y_offsets['IBM'] = 5
y_offsets['AAPL'] = -5
y_offsets['AMZN'] = -6
```

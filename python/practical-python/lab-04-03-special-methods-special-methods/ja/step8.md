# 演習 4.9：オブジェクトの印刷時のより良い出力

`stock.py` で定義した `Stock` オブジェクトを変更して、`__repr__()` メソッドがより有用な出力を生成するようにします。たとえば：

```python
>>> goog = stock.Stock('GOOG', 100, 490.1)
>>> goog
Stock('GOOG', 100, 490.1)
>>>
```

これらの変更を行った後、株式のポートフォリオを読み込み、結果のリストを表示したときに何が起こるか見てみましょう。たとえば：

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> portfolio
... 出力がどのようになるか見る...
>>>
```

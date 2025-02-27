# 等張回帰モデルをフィットさせる

これで、等張回帰モデルをデータにフィットさせることができます。`IsotonicRegression`クラスのインスタンスを作成し、入力データとターゲット値を使って`fit`メソッドを呼び出します。

```python
# Fit isotonic regression model
ir = IsotonicRegression()
ir.fit(X, y)
```

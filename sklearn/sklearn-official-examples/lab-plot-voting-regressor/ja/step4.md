# 予測の実行

次に、それぞれの回帰器を使って最初の20個の予測を行います。

```python
# Make predictions
xt = X[:20]

pred1 = reg1.predict(xt)
pred2 = reg2.predict(xt)
pred3 = reg3.predict(xt)
pred4 = ereg.predict(xt)
```

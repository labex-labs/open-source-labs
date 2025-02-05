# 进行预测

现在我们将使用每个回归器进行前20个预测。

```python
# 进行预测
xt = X[:20]

pred1 = reg1.predict(xt)
pred2 = reg2.predict(xt)
pred3 = reg3.predict(xt)
pred4 = ereg.predict(xt)
```

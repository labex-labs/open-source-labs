# Предсказание

Теперь мы будем использовать каждый из регрессоров для получения первых 20 предсказаний.

```python
# Make predictions
xt = X[:20]

pred1 = reg1.predict(xt)
pred2 = reg2.predict(xt)
pred3 = reg3.predict(xt)
pred4 = ereg.predict(xt)
```

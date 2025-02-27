# Vorhersagen treffen

Jetzt werden wir jeden der Regressoren verwenden, um die ersten 20 Vorhersagen zu treffen.

```python
# Make predictions
xt = X[:20]

pred1 = reg1.predict(xt)
pred2 = reg2.predict(xt)
pred3 = reg3.predict(xt)
pred4 = ereg.predict(xt)
```

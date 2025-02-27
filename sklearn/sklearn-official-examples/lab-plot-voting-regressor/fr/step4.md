# Effectuer des prédictions

Maintenant, nous utiliserons chacun des régresseurs pour effectuer les 20 premières prédictions.

```python
# Make predictions
xt = X[:20]

pred1 = reg1.predict(xt)
pred2 = reg2.predict(xt)
pred3 = reg3.predict(xt)
pred4 = ereg.predict(xt)
```

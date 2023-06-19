# Making Predictions

Now we will use each of the regressors to make the 20 first predictions.

```python
# Make predictions
xt = X[:20]

pred1 = reg1.predict(xt)
pred2 = reg2.predict(xt)
pred3 = reg3.predict(xt)
pred4 = ereg.predict(xt)
```



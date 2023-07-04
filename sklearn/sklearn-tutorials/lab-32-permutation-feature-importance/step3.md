# Evaluate the model

We will now evaluate the trained model using the validation set. The evaluation metric used here is the R-squared score.

```python
# Evaluate the model on the validation set
score = model.score(X_val, y_val)
print("Validation score:", score)
```

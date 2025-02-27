# 予測を行う

分類器の訓練が完了したら、テストデータに対して予測を行うために使用することができます。

```python
# Make predictions on the test data
y_pred = clf.predict(X_test)

# Print the predicted values
print("Predicted values:", y_pred)
```

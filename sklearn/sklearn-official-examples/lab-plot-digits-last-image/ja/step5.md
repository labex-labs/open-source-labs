# モデルの評価

モデルの性能を評価するには、scikit-learnの`accuracy_score`関数を使うことができます。

```python
from sklearn.metrics import accuracy_score

# Predict the labels of the test set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy of the model
print("Accuracy:", accuracy)
```

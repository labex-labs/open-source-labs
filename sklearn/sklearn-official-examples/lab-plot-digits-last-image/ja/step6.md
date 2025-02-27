# モデルの改善

モデルの精度が不十分な場合、SVMアルゴリズムのハイパーパラメータを調整することで改善を試みることができます。たとえば、`C`パラメータの値を変更することを試してみることができます。

```python
# Create the SVM classifier with a different value of C
clf = SVC(kernel='linear', C=0.1)

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy of the model
print("Accuracy:", accuracy)
```

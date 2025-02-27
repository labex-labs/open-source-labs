# 決定木分類器を作成して訓練する

これで、訓練データを使用して決定木（Decision Tree）分類器を作成し、訓練することができます。

```python
# Create a Decision Tree classifier
clf = tree.DecisionTreeClassifier()

# Train the classifier
clf.fit(X_train, y_train)
```

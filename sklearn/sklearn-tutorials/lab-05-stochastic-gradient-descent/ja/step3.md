# SGDを使って分類器を訓練する

今度は、SGDClassifierクラスを使って分類器を訓練します。log_loss損失関数とl2ペナルティを使用します。

```python
# SGDを使って分類器を訓練する
clf = SGDClassifier(loss="log_loss", penalty="l2", max_iter=100, random_state=42)
clf.fit(X_train, y_train)

# テストセットに対する予測を行う
y_pred = clf.predict(X_test)

# 分類器の精度を測定する
accuracy = accuracy_score(y_test, y_pred)

# 精度を表示する
print("Classifier Accuracy:", accuracy)
```

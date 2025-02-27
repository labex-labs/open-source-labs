# モデルの評価

訓練データセットとテストデータセットでの精度を計算することで、MLPClassifier を評価します。

```python
print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))
```

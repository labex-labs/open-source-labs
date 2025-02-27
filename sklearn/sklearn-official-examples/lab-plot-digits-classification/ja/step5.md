# サポートベクターマシンを学習する

`sklearn` の `svm.SVC()` メソッドを使用して、学習用サンプルに対してサポートベクター分類器を学習します。

```python
clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)
```

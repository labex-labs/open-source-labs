# モデルを学習する

このステップでは、生成したデータを使用して、RBF カーネルを持つ SVM 分類器を学習させます。

```python
clf = svm.NuSVC(gamma="auto")
clf.fit(X, Y)
```

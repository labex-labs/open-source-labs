# モデルの作成

このステップでは、線形、多項式、ラジアルベース関数 (RBF) の 3 種類の異なるカーネルを持つ SVM カーネルモデルを作成します。線形カーネルは線形に分離可能なデータポイントに使用され、多項式カーネルと RBF カーネルは非線形に分離可能なデータポイントに役立ちます。

```python
# fit the model
for kernel in ("linear", "poly", "rbf"):
    clf = svm.SVC(kernel=kernel, gamma=2)
    clf.fit(X, Y)
```

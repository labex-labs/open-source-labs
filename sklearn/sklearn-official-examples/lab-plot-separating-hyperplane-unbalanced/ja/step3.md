# モデルの適合

`svm` ライブラリの `SVC` 関数を使って、モデルを適合させ、分離超平面を取得します。線形カーネルを使用し、`C` を 1.0 に設定します。

```python
clf = svm.SVC(kernel="linear", C=1.0)
clf.fit(X, y)
```

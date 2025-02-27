# 重み付きクラスでモデルを適合させる

`svm` ライブラリの `SVC` 関数を使って、モデルを適合させ、分離超平面を取得します。線形カーネルを使用し、`class_weight` を `{1: 10}` に設定します。これにより、小さなクラスにより多くの重みが与えられます。

```python
wclf = svm.SVC(kernel="linear", class_weight={1: 10})
wclf.fit(X, y)
```

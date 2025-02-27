# モデルの適合

scikit-learn の `SVC` クラスを使って SVM モデルを適合させます。カーネルを線形に設定し、ペナルティパラメータ `C` を、正則化なしの場合には 1、正則化ありの場合には 0.05 に設定します。そして、モデルの係数と切片を使って分離超平面を計算します。

```python
for name, penalty in (("unreg", 1), ("reg", 0.05)):
    clf = svm.SVC(kernel="linear", C=penalty)
    clf.fit(X, Y)

    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-5, 5)
    yy = a * xx - (clf.intercept_[0]) / w[1]
```

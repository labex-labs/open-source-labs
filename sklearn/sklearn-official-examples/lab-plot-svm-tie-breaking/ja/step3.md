# バイアス解消を有効にした場合と無効にした場合の SVM モデルを作成する

このステップでは、2 つの SVM モデルを作成します。1 つはバイアス解消を無効にしたもので、もう 1 つはバイアス解消を有効にしたものです。これらのモデルを作成するために、scikit-learn の`SVC`クラスを使用します。2 つのモデルに対して、それぞれ`break_ties`パラメータを`False`と`True`に設定します。

```python
for break_ties, title, ax in zip((False, True), titles, sub.flatten()):
    svm = SVC(
        kernel="linear", C=1, break_ties=break_ties, decision_function_shape="ovr"
    ).fit(X, y)
```

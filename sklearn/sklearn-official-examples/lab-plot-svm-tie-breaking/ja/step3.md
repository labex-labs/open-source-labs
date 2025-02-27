# バイアス解消を有効にした場合と無効にした場合のSVMモデルを作成する

このステップでは、2つのSVMモデルを作成します。1つはバイアス解消を無効にしたもので、もう1つはバイアス解消を有効にしたものです。これらのモデルを作成するために、scikit-learnの`SVC`クラスを使用します。2つのモデルに対して、それぞれ`break_ties`パラメータを`False`と`True`に設定します。

```python
for break_ties, title, ax in zip((False, True), titles, sub.flatten()):
    svm = SVC(
        kernel="linear", C=1, break_ties=break_ties, decision_function_shape="ovr"
    ).fit(X, y)
```

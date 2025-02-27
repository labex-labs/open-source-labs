# SVM 分類器の作成

このステップでは、SVM 分類器のインスタンスを作成してデータに適合させます。前のステップで作成したカスタムカーネルを使用します。

```python
clf = svm.SVC(kernel=my_kernel)
clf.fit(X, Y)
```

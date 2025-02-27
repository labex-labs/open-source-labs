# SVM モデルを適合させる

次に、線形カーネルと正則化パラメータ 1000 を使って SVM モデルをデータセットに適合させます。scikit-learn の `svm.SVC()` 関数を使って SVM 分類器を作成します。

```python
from sklearn import svm

# fit the SVM model
clf = svm.SVC(kernel="linear", C=1000)
clf.fit(X, y)
```

# SVM分類器をセットアップする

放射基底関数（RBF）カーネルを持つSVM分類器をセットアップします。SVMは、教師あり学習アルゴリズムであり、データを異なるクラスに分離する最適なハイパープレーンを見つけます。

```python
from sklearn.svm import SVC

# Set up the SVM classifier
rbf_svc = (SVC(kernel="rbf", gamma=0.5).fit(X, y), y, "SVC with rbf kernel")
```

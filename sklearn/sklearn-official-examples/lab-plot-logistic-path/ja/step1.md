# Iris データセットを読み込む

scikit-learn ライブラリから Iris データセットを読み込みます。このデータセットには、がく片の長さ、がく片の幅、花弁の長さ、花弁の幅の 4 つの特徴が含まれています。二値分類には最初の 2 つの特徴のみを使用します。

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y!= 2] # 二値分類には最初の 2 つの特徴のみを使用
y = y[y!= 2]

X /= X.max() # 収束を加速するために X を正規化
```

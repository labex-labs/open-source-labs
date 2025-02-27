# データの読み込み

Scikit-Learnの`datasets`モジュールを使ってアヤメのデータセットを読み込みます。2つの特徴量のみを使用します：がく片の長さと花弁の長さ。

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, [0, 2]]
y = iris.target
```

# データセットの読み込み

最初のステップは、scikit-learn からアヤメのデータセットを読み込むことです。

```python
from sklearn.datasets import load_iris

# Load the dataset
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
```

# データセットを読み込む

次に、対象となるデータセットを読み込みましょう。この演習では、好きなデータセットを使用できます。

```python
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Split the data into features and target
X = iris.data
y = iris.target
```

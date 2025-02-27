# データセットの読み込み

まず、scikit-learn の組み込み関数 `load_iris()` を使って Iris データセットを読み込む必要があります。

```python
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names
```

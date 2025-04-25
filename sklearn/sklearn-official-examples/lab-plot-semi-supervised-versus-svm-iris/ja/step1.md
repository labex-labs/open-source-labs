# Iris データセットを読み込んでデータを分割する

機械学習における分類タスクで広く使用される Iris データセットを読み込みます。このデータセットには、Iris の花の 150 個のサンプルが含まれており、各サンプルには 4 つの特徴量があります。花弁の長さ、花弁の幅、花びらの長さ、花びらの幅です。このデータセットを入力特徴量とターゲットラベルに分割します。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()

# Split the dataset into input features and target labels
X = iris.data[:, :2] # We will only use the first two features for visualization purposes
y = iris.target
```

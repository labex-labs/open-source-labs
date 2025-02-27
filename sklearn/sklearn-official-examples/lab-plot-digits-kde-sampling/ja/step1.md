# データの読み込み

まず、scikit-learn から digits データセットを読み込みます。このデータセットには、0 から 9 までの数字の 8x8 画像が含まれています。データセットの次元を 15 に削減するために、主成分分析 (Principal Component Analysis: PCA) を使用します。

```python
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# load the digits dataset
digits = load_digits()

# reduce the dimension of the dataset to 15 using PCA
pca = PCA(n_components=15, whiten=False)
data = pca.fit_transform(digits.data)
```

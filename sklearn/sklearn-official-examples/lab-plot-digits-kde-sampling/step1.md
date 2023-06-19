# Load Data

First, we load the digits dataset from scikit-learn. This dataset contains 8x8 images of digits from 0 to 9. We will use Principal Component Analysis (PCA) to reduce the dimension of the dataset to 15.

```python
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# load the digits dataset
digits = load_digits()

# reduce the dimension of the dataset to 15 using PCA
pca = PCA(n_components=15, whiten=False)
data = pca.fit_transform(digits.data)
```



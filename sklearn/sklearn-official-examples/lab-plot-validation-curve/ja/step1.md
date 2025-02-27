# データセットの読み込み

scikit-learn から digits データセットを読み込み、データのサブセットを選択して、数字 1 と 2 の 2 値分類を行います。

```python
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
subset_mask = np.isin(y, [1, 2])  # binary classification: 1 vs 2
X, y = X[subset_mask], y[subset_mask]
```

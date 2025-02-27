# データセットの読み込み

scikit-learnの`fetch_california_housing`関数を使って、サンフランシスコの住宅価格データセットを読み込みます。このデータセットは20,640個のサンプルと8つの特徴量で構成されています。

```python
from sklearn.datasets import fetch_california_housing

X, y = fetch_california_housing(return_X_y=True, as_frame=True)
n_samples, n_features = X.shape

print(f"The dataset consists of {n_samples} samples and {n_features} features")
```

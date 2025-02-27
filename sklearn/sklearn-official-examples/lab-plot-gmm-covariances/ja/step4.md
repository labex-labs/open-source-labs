# 異なる共分散タイプの GMM 推定器の設定

```python
colors = ["navy", "turquoise", "darkorange"]
n_classes = len(np.unique(y_train))

estimators = {
    cov_type: GaussianMixture(
        n_components=n_classes, covariance_type=cov_type, max_iter=20, random_state=0
    )
    for cov_type in ["spherical", "diag", "tied", "full"]
}

n_estimators = len(estimators)
```

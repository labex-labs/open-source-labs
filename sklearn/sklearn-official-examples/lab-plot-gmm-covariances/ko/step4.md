# 서로 다른 공분산 유형에 대한 GMM 추정기 설정

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

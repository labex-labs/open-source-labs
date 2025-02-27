# テストデータ上の尤度を計算する

`sklearn.covariance`モジュールの`ShrunkCovariance`クラスと`scipy.linalg`モジュールの`log_likelihood`関数を使用して、テストデータ上の負の対数尤度を計算します。縮小係数の可能な値の範囲を設定し、各値に対する尤度を計算します。

```python
from sklearn.covariance import ShrunkCovariance, empirical_covariance, log_likelihood
from scipy import linalg

shrinkages = np.logspace(-2, 0, 30)
negative_logliks = [
    -ShrunkCovariance(shrinkage=s).fit(X_train).score(X_test) for s in shrinkages
]

real_cov = np.dot(coloring_matrix.T, coloring_matrix)
emp_cov = empirical_covariance(X_train)
loglik_real = -log_likelihood(emp_cov, linalg.inv(real_cov))
```

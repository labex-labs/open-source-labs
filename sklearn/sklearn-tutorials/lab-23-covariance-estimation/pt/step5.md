# Estimativa Robusta de Covariância

Datasets do mundo real frequentemente contêm outliers ou erros de medição que podem influenciar significativamente a matriz de covariância estimada. Métodos de estimativa de covariância robusta, como o Minimum Covariance Determinant (MCD), podem ser usados para lidar com essas situações. O pacote `sklearn.covariance` fornece uma classe `MinCovDet` para calcular a estimativa MCD.

```python
from sklearn.covariance import MinCovDet

# Criar um objeto MinCovDet e ajustá-lo aos dados
min_cov_det = MinCovDet().fit(data)

# Calcular a matriz de covariância robusta
robust_covariance_matrix = min_cov_det.covariance_
```

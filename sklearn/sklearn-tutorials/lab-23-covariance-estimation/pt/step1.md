# Covariância Empírica

A matriz de covariância empírica é um método comumente utilizado para estimar a matriz de covariância de um conjunto de dados. Baseia-se no princípio da estimação de máxima verossimilhança e assume que as observações são independentes e identicamente distribuídas (i.i.d.). A função `empirical_covariance` no pacote `sklearn.covariance` pode ser usada para calcular a matriz de covariância empírica de um conjunto de dados dado.

```python
from sklearn.covariance import empirical_covariance

# Calcular a matriz de covariância empírica
covariance_matrix = empirical_covariance(data)
```

# Estimer la covariance

La deuxième étape consiste à estimer la covariance. Nous utilisons GraphicalLassoCV pour apprendre la matrice de précision sparse. Nous comparons également les résultats avec l'estimateur Ledoit-Wolf.

```python
from sklearn.covariance import GraphicalLassoCV, ledoit_wolf

emp_cov = np.dot(X.T, X) / n_samples

model = GraphicalLassoCV()
model.fit(X)
cov_ = model.covariance_
prec_ = model.precision_

lw_cov_, _ = ledoit_wolf(X)
lw_prec_ = linalg.inv(lw_cov_)
```

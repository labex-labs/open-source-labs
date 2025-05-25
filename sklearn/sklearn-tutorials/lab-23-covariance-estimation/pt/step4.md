# Estimativa de Covariância Inversa Esparsa

A estimativa de covariância inversa esparsa, também conhecida como seleção de covariância, visa estimar uma matriz de precisão esparsa, onde a inversa da matriz de covariância representa a matriz de correlação parcial. O pacote `sklearn.covariance` inclui uma classe `GraphicalLasso` para estimar a matriz de covariância inversa esparsa usando uma penalidade l1.

```python
from sklearn.covariance import GraphicalLasso

# Criar um objeto GraphicalLasso e ajustá-lo aos dados
graphical_lasso = GraphicalLasso().fit(data)

# Calcular a matriz de covariância inversa esparsa
sparse_inverse_covariance_matrix = graphical_lasso.precision_
```

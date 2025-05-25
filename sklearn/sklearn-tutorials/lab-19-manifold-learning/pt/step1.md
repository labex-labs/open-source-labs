# Isomap

O algoritmo Isomap é uma das primeiras abordagens ao aprendizado de variedades. Ele busca uma incorporação de menor dimensão que mantenha as distâncias geodésicas entre todos os pontos.

```python
from sklearn.manifold import Isomap

# Crie uma instância do algoritmo Isomap
isomap = Isomap(n_components=2)

# Ajuste o algoritmo aos dados e transforme os dados para o espaço de menor dimensão
X_transformed = isomap.fit_transform(X)
```

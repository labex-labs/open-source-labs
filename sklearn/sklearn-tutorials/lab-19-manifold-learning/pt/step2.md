# Embedding Localmente Linear (LLE)

O Embedding Localmente Linear (LLE) é outro algoritmo de aprendizado de variedades. Ele busca uma projeção de menor dimensão dos dados que preserve as distâncias dentro dos vizinhos locais.

```python
from sklearn.manifold import LocallyLinearEmbedding

# Crie uma instância do algoritmo LLE
lle = LocallyLinearEmbedding(n_components=2)

# Ajuste o algoritmo aos dados e transforme os dados para o espaço de menor dimensão
X_transformed = lle.fit_transform(X)
```

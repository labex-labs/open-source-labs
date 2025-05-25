# t-distributed Stochastic Neighbor Embedding (t-SNE)

t-SNE é um método popular de aprendizado de variedades que converte afinidades de pontos de dados em probabilidades. É particularmente eficaz na visualização de dados de alta dimensão.

```python
from sklearn.manifold import TSNE

# Crie uma instância do algoritmo t-SNE
tsne = TSNE(n_components=2)

# Ajuste o algoritmo aos dados e transforme os dados para o espaço de menor dimensão
X_transformed = tsne.fit_transform(X)
```

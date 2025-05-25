# Análise de Componentes Principais (PCA)

#### PCA Exata e Interpretação Probabilística

A Análise de Componentes Principais (PCA) é usada para decompor um conjunto de dados multivariados em um conjunto de componentes ortogonais sucessivos que explicam a maior quantidade possível de variância. A PCA pode ser implementada usando a classe `PCA` do scikit-learn. O método `fit` é usado para aprender os componentes, e o método `transform` pode ser usado para projetar novos dados nesses componentes.

```python
from sklearn.decomposition import PCA

# Crie um objeto PCA com n_components como o número de componentes desejados
pca = PCA(n_components=2)

# Ajuste o modelo PCA aos dados
pca.fit(data)

# Transforme os dados projetando-os nos componentes aprendidos
transformed_data = pca.transform(data)
```

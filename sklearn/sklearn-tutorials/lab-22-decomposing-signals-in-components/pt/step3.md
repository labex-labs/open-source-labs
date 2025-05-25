# Fatoração de Matriz Não-Negativa (NMF)

#### NMF com a norma de Frobenius

A Fatoração de Matriz Não-Negativa (NMF) é uma abordagem alternativa à decomposição que assume dados e componentes não-negativos. Encontra uma decomposição dos dados em duas matrizes de elementos não-negativos, otimizando a distância entre os dados e o produto matricial das duas matrizes. A NMF pode ser implementada usando a classe `NMF` do scikit-learn.

```python
from sklearn.decomposition import NMF

# Crie um objeto NMF com n_components como o número de componentes desejados
nmf = NMF(n_components=2)

# Ajuste o modelo NMF aos dados
nmf.fit(data)

# Decomponha os dados nas duas matrizes não-negativas
matrix_W = nmf.transform(data)
matrix_H = nmf.components_
```

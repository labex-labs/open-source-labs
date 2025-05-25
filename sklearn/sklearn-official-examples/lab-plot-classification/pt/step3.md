# Preparação dos dados

Utilizaremos apenas as duas primeiras características do conjunto de dados Iris, que são a largura e o comprimento da sépala. Em seguida, dividiremos os dados na matriz de características `X` e no vetor alvo `y`.

```python
X = iris.data[:, :2]
y = iris.target
```

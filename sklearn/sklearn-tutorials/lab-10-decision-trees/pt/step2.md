# Carregar o Conjunto de Dados

Em seguida, carregaremos o conjunto de dados Iris. Este conjunto de dados contém informações sobre quatro características de três espécies diferentes de flores Iris. Usaremos este conjunto de dados para treinar nosso classificador de Árvore de Decisão.

```python
# Carregar o conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target
```

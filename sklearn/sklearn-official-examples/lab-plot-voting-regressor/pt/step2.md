# Carregar o Conjunto de Dados de Diabetes

Em seguida, carregaremos o conjunto de dados de diabetes em nosso programa usando a função `load_diabetes()` fornecida pelo scikit-learn. Esta função retorna o conjunto de dados como uma tupla de dois arrays - um contendo os dados das características e outro contendo os dados do alvo. Atribuiremos esses arrays a `X` e `y`, respectivamente.

```python
# Carregar o conjunto de dados de diabetes
X, y = load_diabetes(return_X_y=True)
```

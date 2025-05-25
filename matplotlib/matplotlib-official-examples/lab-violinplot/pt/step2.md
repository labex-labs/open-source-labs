# Criar um conjunto de dados de amostra

Criaremos um conjunto de dados de amostra usando a biblioteca numpy. Criaremos seis conjuntos de dados com diferentes desvios padrão.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# fake data
pos = [1, 2, 4, 5, 7, 8]
data = [np.random.normal(0, std, size=100) for std in pos]
```

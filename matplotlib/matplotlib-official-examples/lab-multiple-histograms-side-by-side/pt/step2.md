# Criar conjuntos de dados de exemplo

Em seguida, criaremos conjuntos de dados de exemplo para usar em nossos histogramas. Criaremos três conjuntos de dados com 387 pontos de dados cada:

```python
np.random.seed(19680801)
number_of_data_points = 387
labels = ["A", "B", "C"]
data_sets = [np.random.normal(0, 1, number_of_data_points),
             np.random.normal(6, 1, number_of_data_points),
             np.random.normal(-3, 1, number_of_data_points)]
```

# Gerar um Conjunto de Dados de Classificação Binária

Em seguida, geraremos um conjunto de dados de classificação binária utilizando a função `make_classification` fornecida pela scikit-learn. Esta função permite especificar o número de amostras, características, clusters por classe e características informativas. Usaremos um valor fixo de estado aleatório para garantir a reprodutibilidade.

```python
X, y = make_classification(
    n_samples=500,
    n_features=25,
    n_clusters_per_class=1,
    n_informative=15,
    random_state=RANDOM_STATE,
)
```

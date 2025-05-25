# Pontuação do Teste de Permutação em Dados Aleatórios

Em seguida, calculamos a `permutation_test_score` usando os recursos aleatoriamente gerados e as etiquetas de classe do conjunto de dados iris, que teoricamente não devem apresentar dependência entre os recursos e as etiquetas.

```python
score_rand, perm_scores_rand, pvalue_rand = permutation_test_score(
    clf, X_rand, y, scoring="accuracy", cv=cv, n_permutations=1000
)
```

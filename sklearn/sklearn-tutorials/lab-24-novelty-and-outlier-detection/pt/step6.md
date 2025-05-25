# Acessar pontuações de valores discrepantes

Além de prever valores discrepantes, também podemos acessar as pontuações de valores discrepantes para cada observação usando o atributo `negative_outlier_factor_`. Pontuações de valores discrepantes mais baixas indicam maior anormalidade.

```python
outlier_scores = estimator.negative_outlier_factor_
print(outlier_scores)
```

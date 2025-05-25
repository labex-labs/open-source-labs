# Treinar Lasso em Dados Densos

Agora, treinamos dois modelos de regressão Lasso, um nos dados densos e outro nos dados esparsos. Definimos o parâmetro alpha para 1 e o número máximo de iterações para 1000.

```python
alpha = 1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
```

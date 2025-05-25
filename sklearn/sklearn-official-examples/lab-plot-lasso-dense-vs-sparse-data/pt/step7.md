# Treinar Lasso em Dados Esparsos

Agora, treinamos dois modelos de regressão Lasso, um nos dados densos e outro nos dados esparsos. Definimos o parâmetro alpha para 0,1 e o número máximo de iterações para 10000.

```python
alpha = 0.1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
```

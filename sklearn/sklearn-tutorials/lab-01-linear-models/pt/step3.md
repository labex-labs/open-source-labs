# Lasso

Lasso é um método de regressão linear que adiciona um termo de penalidade à função objetivo dos mínimos quadrados ordinários. O termo de penalidade tem o efeito de definir alguns coeficientes exatamente em zero, realizando assim a seleção de características. Lasso pode ser usado para estimativa de modelos esparsos.

Vamos ajustar um modelo Lasso.

```python
reg = linear_model.Lasso(alpha=0.1)
reg.fit([[0, 0], [1, 1]], [0, 1])

print(reg.coef_)
```

- Criamos uma instância de `Lasso` com o parâmetro de regularização `alpha` definido como 0,1.
- Usamos o método `fit` para ajustar o modelo aos dados de treinamento.
- Imprimimos os coeficientes do modelo Lasso.

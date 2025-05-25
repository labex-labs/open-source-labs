# Regressão Ridge

A regressão Ridge é um método de regressão linear que adiciona um termo de penalidade à função objetivo dos mínimos quadrados ordinários. Este termo de penalidade ajuda a reduzir o sobreajuste, encolhendo os coeficientes em direção a zero. A complexidade do modelo pode ser controlada pelo parâmetro de regularização.

Vamos ajustar um modelo de regressão Ridge.

```python
reg = linear_model.Ridge(alpha=0.5)
reg.fit([[0, 0], [0, 0], [1, 1]], [0, 0.1, 1])

print(reg.coef_)
```

- Criamos uma instância de `Ridge` com o parâmetro de regularização `alpha` definido como 0,5.
- Usamos o método `fit` para ajustar o modelo aos dados de treinamento.
- Imprimimos os coeficientes do modelo de regressão Ridge.

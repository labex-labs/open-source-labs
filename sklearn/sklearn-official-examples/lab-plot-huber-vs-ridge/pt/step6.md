# Ajustar o Regressor Ridge

Agora, ajustaremos o regressor Ridge ao conjunto de dados e compararemos seu desempenho com o do HuberRegressor.

```python
# Ajustar um regressor ridge para compará-lo ao regressor huber.
ridge = Ridge(alpha=0.0, random_state=0)
ridge.fit(X, y)
coef_ridge = ridge.coef_
coef_ = ridge.coef_ * x + ridge.intercept_
plt.plot(x, coef_, "g-", label="regressão ridge")

# Adicionar uma legenda ao gráfico
plt.legend(loc=0)

# Mostrar o gráfico
plt.title("Comparação de HuberRegressor vs Ridge")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```

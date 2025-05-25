# Plotar os Resultados

Finalmente, visualizaremos as 20 previsões. As estrelas vermelhas mostram a previsão média feita pelo Regressor de Votação.

```python
# Plotar os resultados
plt.figure()
plt.plot(pred1, "gd", label="GradientBoostingRegressor")
plt.plot(pred2, "b^", label="RandomForestRegressor")
plt.plot(pred3, "ys", label="LinearRegression")
plt.plot(pred4, "r*", ms=10, label="VotingRegressor")

plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
plt.ylabel("previsto")
plt.xlabel("amostras de treino")
plt.legend(loc="best")
plt.title("Previsões dos Regressores e sua média")

plt.show()
```

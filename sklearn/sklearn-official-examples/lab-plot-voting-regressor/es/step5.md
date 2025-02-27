# Graficar los resultados

Finalmente, visualizaremos las 20 predicciones. Las estrellas rojas muestran la predicción promedio realizada por el Voting Regressor.

```python
# Graficar los resultados
plt.figure()
plt.plot(pred1, "gd", label="GradientBoostingRegressor")
plt.plot(pred2, "b^", label="RandomForestRegressor")
plt.plot(pred3, "ys", label="LinearRegression")
plt.plot(pred4, "r*", ms=10, label="VotingRegressor")

plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)
plt.ylabel("predicho")
plt.xlabel("muestras de entrenamiento")
plt.legend(loc="best")
plt.title("Predicciones de los regresores y su promedio")

plt.show()
```

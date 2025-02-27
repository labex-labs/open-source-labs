# Graficar la desviación de entrenamiento

Finalmente, visualizaremos los resultados. Para hacer eso, primero calcularemos la desviación del conjunto de prueba y luego la graficaremos en función de las iteraciones de boosting.

```python
test_score = np.zeros((params["n_estimators"],), dtype=np.float64)
for i, y_pred in enumerate(reg.staged_predict(X_test)):
    test_score[i] = mean_squared_error(y_test, y_pred)

fig = plt.figure(figsize=(6, 6))
plt.subplot(1, 1, 1)
plt.title("Desviación")
plt.plot(
    np.arange(params["n_estimators"]) + 1,
    reg.train_score_,
    "b-",
    label="Desviación del Conjunto de Entrenamiento",
)
plt.plot(
    np.arange(params["n_estimators"]) + 1, test_score, "r-", label="Desviación del Conjunto de Prueba"
)
plt.legend(loc="upper right")
plt.xlabel("Iteraciones de Boosting")
plt.ylabel("Desviación")
fig.tight_layout()
plt.show()
```

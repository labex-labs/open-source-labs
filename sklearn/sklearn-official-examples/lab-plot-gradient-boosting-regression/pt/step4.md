# Plotar a Desvio de Treinamento

Finalmente, visualizaremos os resultados. Para isso, primeiro calculamos o desvio do conjunto de teste e, em seguida, plotamos-o contra as iterações de aumento.

```python
test_score = np.zeros((params["n_estimators"],), dtype=np.float64)
for i, y_pred in enumerate(reg.staged_predict(X_test)):
    test_score[i] = mean_squared_error(y_test, y_pred)

fig = plt.figure(figsize=(6, 6))
plt.subplot(1, 1, 1)
plt.title("Desvio")
plt.plot(
    np.arange(params["n_estimators"]) + 1,
    reg.train_score_,
    "b-",
    label="Desvio do Conjunto de Treinamento",
)
plt.plot(
    np.arange(params["n_estimators"]) + 1, test_score, "r-", label="Desvio do Conjunto de Teste"
)
plt.legend(loc="upper right")
plt.xlabel("Iterações de Aumento")
plt.ylabel("Desvio")
fig.tight_layout()
plt.show()
```

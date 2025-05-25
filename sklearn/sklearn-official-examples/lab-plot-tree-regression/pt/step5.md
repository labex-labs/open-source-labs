# Plotar os resultados

Vamos plotar os resultados para visualizar como os modelos ajustam os dados.

```python
plt.figure()
plt.scatter(X, y, s=20, edgecolor="black", c="darkorange", label="dados")
plt.plot(X_test, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("dados")
plt.ylabel("alvo")
plt.title("Regressão da Árvore de Decisão")
plt.legend()
plt.show()
```

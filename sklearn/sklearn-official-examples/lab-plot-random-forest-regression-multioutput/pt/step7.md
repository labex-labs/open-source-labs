# Plotar Resultados

Plotaremos os resultados para comparar o desempenho dos dois regressores. Usaremos `matplotlib` para criar um gráfico de dispersão dos dados de teste reais, as previsões feitas pelo regressor random forest e as previsões feitas pelo regressor multi-output.

```python
plt.figure()
s = 50
a = 0.4
plt.scatter(y_test[:, 0], y_test[:, 1], edgecolor="k", c="navy", s=s, marker="s", alpha=a, label="Dados")
plt.scatter(y_rf[:, 0], y_rf[:, 1], edgecolor="k", c="c", s=s, marker="^", alpha=a, label="Desempenho RF=%.2f" % regr_rf.score(X_test, y_test))
plt.scatter(y_multirf[:, 0], y_multirf[:, 1], edgecolor="k", c="cornflowerblue", s=s, alpha=a, label="Desempenho Multi RF=%.2f" % regr_multirf.score(X_test, y_test))
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.xlabel("alvo 1")
plt.ylabel("alvo 2")
plt.title("Comparando Florestas Aleatórias e o Estimador Meta Multi-Saída")
plt.legend()
plt.show()
```

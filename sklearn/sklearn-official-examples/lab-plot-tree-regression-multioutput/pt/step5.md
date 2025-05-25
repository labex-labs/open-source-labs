# Plotar os Resultados

Neste passo, plotaremos os resultados. Usaremos `matplotlib.pyplot` para criar um gráfico de dispersão dos dados originais e das previsões dos três modelos. Também adicionaremos rótulos e título ao gráfico.

```python
# Plotar os resultados
plt.figure()
s = 25
plt.scatter(y[:, 0], y[:, 1], c="navy", s=s, edgecolor="black", label="dados")
plt.scatter(
    y_1[:, 0],
    y_1[:, 1],
    c="cornflowerblue",
    s=s,
    edgecolor="black",
    label="max_depth=2",
)
plt.scatter(y_2[:, 0], y_2[:, 1], c="red", s=s, edgecolor="black", label="max_depth=5")
plt.scatter(
    y_3[:, 0], y_3[:, 1], c="orange", s=s, edgecolor="black", label="max_depth=8"
)
plt.xlim([-6, 6])
plt.ylim([-6, 6])
plt.xlabel("alvo 1")
plt.ylabel("alvo 2")
plt.title("Regressão de Árvore de Decisão Multi-saída")
plt.legend(loc="best")
plt.show()
```

# Visualizar a Taxa de Erro OOB

Finalmente, plotaremos a taxa de erro OOB para cada classificador em função do número de estimadores. Isso nos permitirá identificar o número de estimadores em que a taxa de erro se estabiliza. Usaremos o Matplotlib para gerar o gráfico.

```python
for label, clf_err in error_rate.items():
    xs, ys = zip(*clf_err)
    plt.plot(xs, ys, label=label)

plt.xlim(min_estimators, max_estimators)
plt.xlabel("n_estimators")
plt.ylabel("Taxa de erro OOB")
plt.legend(loc="upper right")
plt.show()
```

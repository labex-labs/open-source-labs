# Plotar as pontuações de decisão das duas classes

Neste passo, plotaremos as pontuações de decisão das duas classes. Usaremos o método `decision_function` do classificador AdaBoost para obter as pontuações de decisão para cada amostra no conjunto de dados. Em seguida, plotaremos os histogramas das pontuações de decisão para cada classe.

```python
# Plotar as pontuações de decisão das duas classes
twoclass_output = bdt.decision_function(X)
plot_range = (twoclass_output.min(), twoclass_output.max())
plt.subplot(122)
for i, n, c in zip(range(2), class_names, plot_colors):
    plt.hist(
        twoclass_output[y == i],
        bins=10,
        range=plot_range,
        facecolor=c,
        label="Classe %s" % n,
        alpha=0.5,
        edgecolor="k",
    )
x1, x2, y1, y2 = plt.axis()
plt.axis((x1, x2, y1, y2 * 1.2))
plt.legend(loc="upper right")
plt.ylabel("Amostras")
plt.xlabel("Pontuação")
plt.title("Pontuações de Decisão")

plt.tight_layout()
plt.subplots_adjust(wspace=0.35)
plt.show()
```

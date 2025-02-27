# Graficar las probabilidades de clase

Graficaremos las probabilidades de clase para cada clasificador y el VotingClassifier utilizando un gráfico de barras.

```python
N = 4  # número de grupos
ind = np.arange(N)  # posiciones de los grupos
width = 0.35  # ancho de las barras

fig, ax = plt.subplots()

# barras para el clasificador 1-3
p1 = ax.bar(ind, np.hstack(([class1_1[:-1], [0]])), width, color="green", edgecolor="k")
p2 = ax.bar(
    ind + width,
    np.hstack(([class2_1[:-1], [0]])),
    width,
    color="lightgreen",
    edgecolor="k",
)

# barras para el VotingClassifier
p3 = ax.bar(ind, [0, 0, 0, class1_1[-1]], width, color="blue", edgecolor="k")
p4 = ax.bar(
    ind + width, [0, 0, 0, class2_1[-1]], width, color="steelblue", edgecolor="k"
)

# anotaciones del gráfico
plt.axvline(2.8, color="k", linestyle="dashed")
ax.set_xticks(ind + width)
ax.set_xticklabels(
    [
        "LogisticRegression\npeso 1",
        "GaussianNB\npeso 1",
        "RandomForestClassifier\npeso 5",
        "VotingClassifier\n(probabilidades promedio)",
    ],
    rotation=40,
    ha="right",
)
plt.ylim([0, 1])
plt.title("Probabilidades de clase para la muestra 1 por diferentes clasificadores")
plt.legend([p1[0], p2[0]], ["clase 1", "clase 2"], loc="upper left")
plt.tight_layout()
plt.show()
```

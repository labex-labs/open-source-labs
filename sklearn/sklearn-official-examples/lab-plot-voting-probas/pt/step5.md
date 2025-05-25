# Plotar as Probabilidades de Classe

Plotaremos as probabilidades de classe para cada classificador e o `VotingClassifier` usando um gráfico de barras.

```python
N = 4  # número de grupos
ind = np.arange(N)  # posições dos grupos
width = 0.35  # largura da barra

fig, ax = plt.subplots()

# barras para os classificadores 1-3
p1 = ax.bar(ind, np.hstack(([class1_1[:-1], [0]])), width, color="green", edgecolor="k")
p2 = ax.bar(
    ind + width,
    np.hstack(([class2_1[:-1], [0]])),
    width,
    color="lightgreen",
    edgecolor="k",
)

# barras para o VotingClassifier
p3 = ax.bar(ind, [0, 0, 0, class1_1[-1]], width, color="blue", edgecolor="k")
p4 = ax.bar(
    ind + width, [0, 0, 0, class2_1[-1]], width, color="steelblue", edgecolor="k"
)

# anotações do gráfico
plt.axvline(2.8, color="k", linestyle="dashed")
ax.set_xticks(ind + width)
ax.set_xticklabels(
    [
        "LogisticRegression\npeso 1",
        "GaussianNB\npeso 1",
        "RandomForestClassifier\npeso 5",
        "VotingClassifier\n(probabilidades médias)",
    ],
    rotation=40,
    ha="right",
)
plt.ylim([0, 1])
plt.title("Probabilidades de classe para a amostra 1 por diferentes classificadores")
plt.legend([p1[0], p2[0]], ["classe 1", "classe 2"], loc="upper left")
plt.tight_layout()
plt.show()
```

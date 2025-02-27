# Tracer les probabilités de classes

Nous allons tracer les probabilités de classes pour chaque classifieur et le VotingClassifier à l'aide d'un graphique à barres.

```python
N = 4  # nombre de groupes
ind = np.arange(N)  # positions des groupes
width = 0.35  # largeur des barres

fig, ax = plt.subplots()

# barres pour le classifieur 1-3
p1 = ax.bar(ind, np.hstack(([class1_1[:-1], [0]])), width, color="green", edgecolor="k")
p2 = ax.bar(
    ind + width,
    np.hstack(([class2_1[:-1], [0]])),
    width,
    color="lightgreen",
    edgecolor="k",
)

# barres pour le VotingClassifier
p3 = ax.bar(ind, [0, 0, 0, class1_1[-1]], width, color="blue", edgecolor="k")
p4 = ax.bar(
    ind + width, [0, 0, 0, class2_1[-1]], width, color="steelblue", edgecolor="k"
)

# annotations du tracé
plt.axvline(2.8, color="k", linestyle="dashed")
ax.set_xticks(ind + width)
ax.set_xticklabels(
    [
        "LogisticRegression\npoids 1",
        "GaussianNB\npoids 1",
        "RandomForestClassifier\npoids 5",
        "VotingClassifier\n(probabilités moyennes)",
    ],
    rotation=40,
    ha="right",
)
plt.ylim([0, 1])
plt.title("Probabilités de classes pour l'échantillon 1 par différents classifieurs")
plt.legend([p1[0], p2[0]], ["classe 1", "classe 2"], loc="upper left")
plt.tight_layout()
plt.show()
```

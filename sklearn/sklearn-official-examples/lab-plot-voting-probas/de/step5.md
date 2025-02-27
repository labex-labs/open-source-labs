# Zeichnen Sie die Klasswahrscheinlichkeiten

Wir werden die Klasswahrscheinlichkeiten für jeden Klassifizierer und den VotingClassifier mithilfe eines Balkendiagramms zeichnen.

```python
N = 4  # Anzahl der Gruppen
ind = np.arange(N)  # Gruppenpositionen
width = 0.35  # Balkenbreite

fig, ax = plt.subplots()

# Balken für Klassifizierer 1-3
p1 = ax.bar(ind, np.hstack(([class1_1[:-1], [0]])), width, color="green", edgecolor="k")
p2 = ax.bar(
    ind + width,
    np.hstack(([class2_1[:-1], [0]])),
    width,
    color="lightgreen",
    edgecolor="k",
)

# Balken für VotingClassifier
p3 = ax.bar(ind, [0, 0, 0, class1_1[-1]], width, color="blue", edgecolor="k")
p4 = ax.bar(
    ind + width, [0, 0, 0, class2_1[-1]], width, color="steelblue", edgecolor="k"
)

# Diagrammanmerkungen
plt.axvline(2.8, color="k", linestyle="dashed")
ax.set_xticks(ind + width)
ax.set_xticklabels(
    [
        "LogisticRegression\nGewicht 1",
        "GaussianNB\nGewicht 1",
        "RandomForestClassifier\nGewicht 5",
        "VotingClassifier\n(durchschnittliche Wahrscheinlichkeiten)",
    ],
    rotation=40,
    ha="right",
)
plt.ylim([0, 1])
plt.title("Klasswahrscheinlichkeiten für Probe 1 durch verschiedene Klassifizierer")
plt.legend([p1[0], p2[0]], ["Klasse 1", "Klasse 2"], loc="upper left")
plt.tight_layout()
plt.show()
```

# Zeichne die Ergebnisse

Wir zeichnen ein Histogramm der Permutations-Scores (die Nullverteilung) für sowohl den ursprünglichen Iris-Datensatz als auch die randomisierten Daten. Wir markieren auch den Score, den der Klassifizierer auf den ursprünglichen Daten erhalten hat, mit einer roten Linie. Der p-Wert wird auf jedem Graphen angezeigt.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Ursprüngliche Daten
ax.hist(perm_scores_iris, bins=20, density=True)
ax.axvline(score_iris, ls="--", color="r")
score_label = f"Score auf ursprünglichen\nDaten: {score_iris:.2f}\n(p-Wert: {pvalue_iris:.3f})"
ax.text(0.7, 10, score_label, fontsize=12)
ax.set_xlabel("Accuracy score")
_ = ax.set_ylabel("Wahrscheinlichkeitsdichte")

plt.show()

fig, ax = plt.subplots()

# Zufällige Daten
ax.hist(perm_scores_rand, bins=20, density=True)
ax.set_xlim(0.13)
ax.axvline(score_rand, ls="--", color="r")
score_label = f"Score auf ursprünglichen\nDaten: {score_rand:.2f}\n(p-Wert: {pvalue_rand:.3f})"
ax.text(0.14, 7.5, score_label, fontsize=12)
ax.set_xlabel("Accuracy score")
ax.set_ylabel("Wahrscheinlichkeitsdichte")

plt.show()
```

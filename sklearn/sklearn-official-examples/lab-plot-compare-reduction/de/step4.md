# Ergebnisse grafisch darstellen

Wir werden die Ergebnisse von `GridSearchCV` mithilfe eines Balkendiagramms darstellen. Dies wird uns ermöglichen, die Genauigkeit unterschiedlicher Merkmalsreduktionstechniken zu vergleichen.

```python
import pandas as pd

mean_scores = np.array(grid.cv_results_["mean_test_score"])
# Die Scores folgen der Reihenfolge der param_grid-Iteration, was alphabetisch ist
mean_scores = mean_scores.reshape(len(C_OPTIONS), -1, len(N_FEATURES_OPTIONS))
# Wähle den Score für das beste C
mean_scores = mean_scores.max(axis=0)
# Erstelle einen DataFrame, um die Grafik zu erleichtern
mean_scores = pd.DataFrame(
    mean_scores.T, index=N_FEATURES_OPTIONS, columns=reducer_labels
)

ax = mean_scores.plot.bar()
ax.set_title("Vergleich von Merkmalsreduktionstechniken")
ax.set_xlabel("Reduzierte Anzahl der Merkmale")
ax.set_ylabel("Genauigkeit der Zifferklassifizierung")
ax.set_ylim((0, 1))
ax.legend(loc="upper left")

plt.show()
```

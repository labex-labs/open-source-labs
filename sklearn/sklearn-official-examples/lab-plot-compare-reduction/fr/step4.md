# Tracer les résultats

Nous allons tracer les résultats de `GridSearchCV` à l'aide d'un graphique en barres. Cela nous permettra de comparer la précision de différentes techniques de réduction de caractéristiques.

```python
import pandas as pd

mean_scores = np.array(grid.cv_results_["mean_test_score"])
# les scores sont dans l'ordre de l'itération de param_grid, qui est alphabétique
mean_scores = mean_scores.reshape(len(C_OPTIONS), -1, len(N_FEATURES_OPTIONS))
# sélectionnez le score pour le meilleur C
mean_scores = mean_scores.max(axis=0)
# créez un DataFrame pour faciliter la tracé
mean_scores = pd.DataFrame(
    mean_scores.T, index=N_FEATURES_OPTIONS, columns=reducer_labels
)

ax = mean_scores.plot.bar()
ax.set_title("Comparaison des techniques de réduction de caractéristiques")
ax.set_xlabel("Nombre réduit de caractéristiques")
ax.set_ylabel("Précision de la classification de chiffres")
ax.set_ylim((0, 1))
ax.legend(loc="upper left")

plt.show()
```

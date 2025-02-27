# Tracer le nombre de caractéristiques en fonction des scores de validation croisée

Nous allons tracer le nombre de caractéristiques sélectionnées en fonction des scores de validation croisée. Nous utiliserons matplotlib pour créer le tracé.

```python
import matplotlib.pyplot as plt

n_scores = len(rfecv.cv_results_["mean_test_score"])
plt.figure()
plt.xlabel("Nombre de caractéristiques sélectionnées")
plt.ylabel("Précision moyenne du test")
plt.errorbar(
    range(min_features_to_select, n_scores + min_features_to_select),
    rfecv.cv_results_["mean_test_score"],
    yerr=rfecv.cv_results_["std_test_score"],
)
plt.title("Élimination Récursive de Caractéristiques \navec des caractéristiques corrélées")
plt.show()
```

# Effectuer la validation croisée et enregistrer les résultats

Pour chaque valeur de C, nous effectuons une validation croisée à 10 plis et enregistrons la moyenne et l'écart-type des scores.

```python
from sklearn.model_selection import cross_val_score

scores = list()
scores_std = list()
for C in C_s:
    svc.C = C
    this_scores = cross_val_score(svc, X, y, n_jobs=1)
    scores.append(np.mean(this_scores))
    scores_std.append(np.std(this_scores))
```

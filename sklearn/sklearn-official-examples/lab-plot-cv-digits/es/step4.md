# Realizar validación cruzada y registrar resultados

Para cada valor de C, realizamos una validación cruzada de 10 pliegues y registramos la media y la desviación estándar de las puntuaciones.

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

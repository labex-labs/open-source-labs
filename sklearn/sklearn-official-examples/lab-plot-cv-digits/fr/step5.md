# Tracer les résultats

Enfin, nous traçons les scores moyens en fonction de C et incluons également des barre d'erreur pour visualiser l'écart-type.

```python
import matplotlib.pyplot as plt

plt.figure()
plt.semilogx(C_s, scores)
plt.semilogx(C_s, np.array(scores) + np.array(scores_std), "b--")
plt.semilogx(C_s, np.array(scores) - np.array(scores_std), "b--")
locs, labels = plt.yticks()
plt.yticks(locs, list(map(lambda x: "%g" % x, locs)))
plt.ylabel("Score de validation croisée")
plt.xlabel("Paramètre C")
plt.ylim(0, 1.1)
plt.show()
```

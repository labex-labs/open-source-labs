# Graficar los resultados

Finalmente, graficamos las puntuaciones promedio en función de C, y también incluimos barras de error para visualizar la desviación estándar.

```python
import matplotlib.pyplot as plt

plt.figure()
plt.semilogx(C_s, scores)
plt.semilogx(C_s, np.array(scores) + np.array(scores_std), "b--")
plt.semilogx(C_s, np.array(scores) - np.array(scores_std), "b--")
locs, labels = plt.yticks()
plt.yticks(locs, list(map(lambda x: "%g" % x, locs)))
plt.ylabel("Puntuación CV")
plt.xlabel("Parámetro C")
plt.ylim(0, 1.1)
plt.show()
```

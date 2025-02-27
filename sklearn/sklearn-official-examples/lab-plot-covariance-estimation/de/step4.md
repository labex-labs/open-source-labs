# Ergebnisse plotten

Wir plotten die Wahrscheinlichkeit für unbekannte Daten für verschiedene Werte des Shrinkage-Parameters und zeigen die Auswahlmöglichkeiten durch Kreuzvalidierung, LedoitWolf- und OAS-Schätzungen.

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.title("Regularisierte Kovarianz: Wahrscheinlichkeit und Shrinkage-Koeffizient")
plt.xlabel("Regularisierungsparameter: Shrinkage-Koeffizient")
plt.ylabel("Fehler: negative Log-Wahrscheinlichkeit auf Testdaten")

plt.loglog(shrinkages, negative_logliks, label="Negative Log-Wahrscheinlichkeit")

plt.plot(plt.xlim(), 2 * [loglik_real], "--r", label="Wahrscheinlichkeit der realen Kovarianz")

lik_max = np.amax(negative_logliks)
lik_min = np.amin(negative_logliks)
ymin = lik_min - 6.0 * np.log((plt.ylim()[1] - plt.ylim()[0]))
ymax = lik_max + 10.0 * np.log(lik_max - lik_min)
xmin = shrinkages[0]
xmax = shrinkages[-1]

plt.vlines(
    lw.shrinkage_,
    ymin,
    -loglik_lw,
    color="magenta",
    linewidth=3,
    label="Ledoit-Wolf-Schätzung",
)

plt.vlines(
    oa.shrinkage_, ymin, -loglik_oa, color="lila", linewidth=3, label="OAS-Schätzung"
)

plt.vlines(
    cv.best_estimator_.shrinkage,
    ymin,
    -cv.best_estimator_.score(X_test),
    color="cyan",
    linewidth=3,
    label="Kreuzvalidierungs-beste Schätzung",
)

plt.ylim(ymin, ymax)
plt.xlim(xmin, xmax)
plt.legend()

plt.show()
```

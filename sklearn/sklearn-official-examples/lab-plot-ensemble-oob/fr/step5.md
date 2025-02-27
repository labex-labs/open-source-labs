# Visualiser le taux d'erreur hors-bag (OOB)

Enfin, nous allons tracer le taux d'erreur hors-bag pour chaque classifieur en fonction du nombre d'estimateurs. Cela nous permettra d'identifier le nombre d'estimateurs à partir duquel le taux d'erreur se stabilise. Nous utiliserons Matplotlib pour générer le tracé.

```python
for label, clf_err in error_rate.items():
    xs, ys = zip(*clf_err)
    plt.plot(xs, ys, label=label)

plt.xlim(min_estimators, max_estimators)
plt.xlabel("n_estimators")
plt.ylabel("Taux d'erreur hors-bag")
plt.legend(loc="upper right")
plt.show()
```

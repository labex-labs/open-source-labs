# Détection d'anomalies sur des données complexes

Nous allons effectuer une détection d'anomalies sur l'ensemble de données Wine en forme de "banane". Nous utiliserons les mêmes trois classifieurs que précédemment et tracerons les résultats.

```python
# Apprenons une frontière pour la détection d'anomalies avec plusieurs classifieurs
xx2, yy2 = np.meshgrid(np.linspace(-1, 5.5, 500), np.linspace(-2.5, 19, 500))
for i, (clf_name, clf) in enumerate(classifiers.items()):
    plt.figure(2)
    clf.fit(X2)
    Z2 = clf.decision_function(np.c_[xx2.ravel(), yy2.ravel()])
    Z2 = Z2.reshape(xx2.shape)
    plt.contour(
        xx2, yy2, Z2, levels=[0], linewidths=2, colors=colors[i]
    )

# Tracez les résultats (= forme du nuage de points de données)
plt.figure(2)  # forme de "banane"
plt.title("Détection d'anomalies sur un ensemble de données réelles (reconnaissance des vins)")
plt.scatter(X2[:, 0], X2[:, 1], color="black")
plt.xlim((xx2.min(), xx2.max()))
plt.ylim((yy2.min(), yy2.max()))
plt.ylabel("intensité de couleur")
plt.xlabel("flavonoïdes")
plt.show()
```

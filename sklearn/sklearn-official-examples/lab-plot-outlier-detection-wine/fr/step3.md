# Détection d'anomalies sur des données bidimensionnelles

Nous allons effectuer une détection d'anomalies sur l'ensemble de données bidimensionnelles Wine. Nous utiliserons trois classifieurs différents pour détecter les anomalies : Empirical Covariance, Robust Covariance et One-Class SVM. Nous tracerons ensuite les résultats.

```python
# Apprenons une frontière pour la détection d'anomalies avec plusieurs classifieurs
xx1, yy1 = np.meshgrid(np.linspace(0, 6, 500), np.linspace(1, 4.5, 500))
for i, (clf_name, clf) in enumerate(classifiers.items()):
    plt.figure(1)
    clf.fit(X1)
    Z1 = clf.decision_function(np.c_[xx1.ravel(), yy1.ravel()])
    Z1 = Z1.reshape(xx1.shape)
    plt.contour(
        xx1, yy1, Z1, levels=[0], linewidths=2, colors=colors[i]
    )

# Tracez les résultats (= forme du nuage de points de données)
plt.figure(1)  # deux grappes
plt.title("Détection d'anomalies sur un ensemble de données réelles (reconnaissance des vins)")
plt.scatter(X1[:, 0], X1[:, 1], color="black")
plt.xlim((xx1.min(), xx1.max()))
plt.ylim((yy1.min(), yy1.max()))
plt.ylabel("cendres")
plt.xlabel("acide malique")
plt.show()
```

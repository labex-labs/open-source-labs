# Effectuer l'ADA

Maintenant, nous effectuerons l'Analyse Discriminante Linéaire (ADA) sur l'ensemble de données pour identifier les attributs qui expliquent la plus grande partie de la variance entre les classes. Contrairement à l'ACP, l'ADA est une méthode supervisée qui utilise les étiquettes de classe connues.

```python
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(X, y).transform(X)

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], alpha=0.8, color=color, label=target_name)

plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("LDA of Iris Dataset")
plt.show()
```

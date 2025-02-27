# Führe LDA durch

Jetzt werden wir die Lineare Diskriminanzanalyse (LDA) auf dem Datensatz durchführen, um Attribute zu identifizieren, die die meiste Varianz zwischen den Klassen erklären. Anders als die PCA ist die LDA eine überwachte Methode, die bekannte Klassenlabels verwendet.

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

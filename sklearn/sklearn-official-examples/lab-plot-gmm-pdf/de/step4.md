# Dichteschätzung darstellen

Wir werden nun die Dichteschätzung der Gaussian-Mischung darstellen. Wir werden ein Gitter von Punkten über den Bereich des Datensatzes erstellen und die negative Log-Likelihood berechnen, die vom GMM für jeden Punkt vorhergesagt wird. Anschließend werden wir die vorhergesagten Scores als Konturplot anzeigen und die Trainingsdaten als Streudiagramm darstellen.

```python
# zeige die von dem Modell vorhergesagten Scores als Konturplot an
x = np.linspace(-20.0, 30.0)
y = np.linspace(-20.0, 40.0)
X, Y = np.meshgrid(x, y)
XX = np.array([X.ravel(), Y.ravel()]).T
Z = -clf.score_samples(XX)
Z = Z.reshape(X.shape)

CS = plt.contour(
    X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0), levels=np.logspace(0, 3, 10)
)
CB = plt.colorbar(CS, shrink=0.8, extend="both")
plt.scatter(X_train[:, 0], X_train[:, 1], 0.8)

plt.title("Dichteschätzung mit Gaussian Mixture Models")
plt.axis("tight")
plt.show()
```

# Kontur plotten

Wir zeichnen die Kontur der Entscheidungsfunktion. Zunächst erstellen wir ein Gitternetz mit den Arrays `xx` und `yy`. Anschließend formen wir das Gitternetz in ein 2D-Array um und wenden die `decision_function`-Methode der `SVC`-Klasse an, um die vorhergesagten Werte zu erhalten. Anschließend zeichnen wir die Kontur mit der `contourf`-Methode.

```python
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

plt.contourf(XX, YY, Z, cmap=plt.get_cmap("RdBu"), alpha=0.5, linestyles=["-"])

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.xticks(())
plt.yticks(())
```

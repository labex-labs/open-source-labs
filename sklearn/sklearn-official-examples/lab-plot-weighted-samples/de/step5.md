# Entscheidungsfunktionen plotten

Wir werden die Entscheidungsfunktionen der beiden gerade erstellten Modelle plotten. Wir werden die Entscheidungsfunktion des ersten Modells links und die Entscheidungsfunktion des zweiten Modells rechts plotten. Die Größe der Punkte wird proportional zu ihrem Gewicht sein.

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

xx, yy = np.meshgrid(np.linspace(-4, 5, 500), np.linspace(-4, 5, 500))
Z = clf_no_weights.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

axes[0].contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.bone)
axes[0].scatter(X[:, 0], X[:, 1], c=y, s=100 * sample_weight_constant, alpha=0.9, cmap=plt.cm.bone, edgecolors="black")
axes[0].axis("off")
axes[0].set_title("Konstante Gewichte")

Z = clf_weights.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

axes[1].contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.bone)
axes[1].scatter(X[:, 0], X[:, 1], c=y, s=100 * sample_weight_last_ten, alpha=0.9, cmap=plt.cm.bone, edgecolors="black")
axes[1].axis("off")
axes[1].set_title("Modifizierte Gewichte")

plt.show()
```

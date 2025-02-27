# Plotten der vorhergesagten Wahrscheinlichkeiten

Jetzt werden wir die vorhergesagten Wahrscheinlichkeiten für jeden Punkt auf dem Gitter plotten. Wir werden zwei Teilplots erstellen: Einen für die isotrope RBF-Kernfunktion und einen für die anisotrope RBF-Kernfunktion. Wir verwenden die `predict_proba`-Methode, um die vorhergesagten Wahrscheinlichkeiten für jeden Punkt auf dem Gitter zu erhalten. Anschließend werden wir die vorhergesagten Wahrscheinlichkeiten als Farbplot auf dem Gitter plotten. Wir werden auch die Trainingspunkte für jede Art von Iris-Blume plotten.

```python
titles = ["Isotropic RBF", "Anisotropic RBF"]
plt.figure(figsize=(10, 5))
for i, clf in enumerate((gpc_rbf_isotropic, gpc_rbf_anisotropic)):
    # Plot the predicted probabilities. For that, we will assign a color to
    # each point in the mesh [x_min, m_max]x[y_min, y_max].
    plt.subplot(1, 2, i + 1)

    Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape((xx.shape[0], xx.shape[1], 3))
    plt.imshow(Z, extent=(x_min, x_max, y_min, y_max), origin="lower")

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=np.array(["r", "g", "b"])[y], edgecolors=(0, 0, 0))
    plt.xlabel("Sepal length")
    plt.ylabel("Sepal width")
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(
        "%s, LML: %.3f" % (titles[i], clf.log_marginal_likelihood(clf.kernel_.theta))
    )

plt.tight_layout()
plt.show()
```

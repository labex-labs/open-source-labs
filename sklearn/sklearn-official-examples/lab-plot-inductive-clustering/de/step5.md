# Vorhersage der Clusterzugehörigkeit für unbekannte Instanzen

In diesem Schritt werden wir das induktive Lernmodell verwenden, um die Clusterzugehörigkeit für die generierten neuen Proben zu prognostizieren. Wir werden die `predict`-Funktion aus der `InductiveClusterer`-Klasse verwenden und die neuen Proben mit ihren wahrscheinlichen Clustern plotten.

```python
probable_clusters = inductive_learner.predict(X_new)

plt.subplot(133)
plot_scatter(X, cluster_labels)
plot_scatter(X_new, probable_clusters)
plt.title("Classify unknown instances")
```

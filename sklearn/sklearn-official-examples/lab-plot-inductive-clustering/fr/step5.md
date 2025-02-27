# Prédire l'appartenance à un cluster pour des instances inconnues

Dans cette étape, nous allons utiliser le modèle d'apprentissage inductif pour prédire l'appartenance à un cluster pour les nouveaux échantillons générés. Nous utiliserons la fonction `predict` de la classe `InductiveClusterer` et tracer les nouveaux échantillons avec leurs clusters probables.

```python
probable_clusters = inductive_learner.predict(X_new)

plt.subplot(133)
plot_scatter(X, cluster_labels)
plot_scatter(X_new, probable_clusters)
plt.title("Classify unknown instances")
```

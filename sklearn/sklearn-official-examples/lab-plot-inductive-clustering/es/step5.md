# Predecir la pertenencia a un cluster para instancias desconocidas

En este paso, usaremos el modelo de aprendizaje inductivo para predecir la pertenencia a un cluster de las nuevas muestras generadas. Usaremos la función `predict` de la clase `InductiveClusterer` y graficaremos las nuevas muestras con sus posibles clusters.

```python
probable_clusters = inductive_learner.predict(X_new)

plt.subplot(133)
plot_scatter(X, cluster_labels)
plot_scatter(X_new, probable_clusters)
plt.title("Classify unknown instances")
```

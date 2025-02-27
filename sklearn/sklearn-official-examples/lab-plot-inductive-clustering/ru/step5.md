# Предсказание принадлежности кластера для неизвестных экземпляров

В этом шаге мы будем использовать модель индуктивного обучения для предсказания принадлежности кластера для сгенерированных новых выборок. Мы будем использовать функцию `predict` из класса `InductiveClusterer` и построить новые выборки с их вероятными кластерами.

```python
probable_clusters = inductive_learner.predict(X_new)

plt.subplot(133)
plot_scatter(X, cluster_labels)
plot_scatter(X_new, probable_clusters)
plt.title("Classify unknown instances")
```

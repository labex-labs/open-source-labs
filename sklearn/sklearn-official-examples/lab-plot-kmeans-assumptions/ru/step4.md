# Возможные решения

Мы обсудим некоторые возможные решения для ограничений кластеризации k-средних. В следующем блоке кода мы показываем, как определить правильное количество кластеров для первого набора данных и как бороться с кластерами различного размера, увеличив количество случайных начальных инициализаций.

```python
y_pred = KMeans(n_clusters=3, **common_params).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("Optimal Number of Clusters")
plt.show()

y_pred = KMeans(n_clusters=3, n_init=10, random_state=random_state).fit_predict(
    X_filtered
)
plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
plt.title("Unevenly Sized Blobs \nwith several initializations")
plt.show()
```

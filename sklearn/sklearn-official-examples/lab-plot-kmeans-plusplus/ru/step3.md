# Построение графиков с начальными точками (seeds) и примерами данных

Мы будем использовать библиотеку matplotlib для построения графиков с начальными точками (seeds) вдоль примерных данных. Начальные точки (seeds) будут показаны как синие точки, а примерные данные - как цветные точки.

```python
# Plot init seeds along side sample data
plt.figure(1)
colors = ["#4EACC5", "#FF9C34", "#4E9A06", "m"]

for k, col in enumerate(colors):
    cluster_data = y_true == k
    plt.scatter(X[cluster_data, 0], X[cluster_data, 1], c=col, marker=".", s=10)

plt.scatter(centers_init[:, 0], centers_init[:, 1], c="b", s=50)
plt.title("K-Means++ Initialization")
plt.xticks([])
plt.yticks([])
plt.show()
```

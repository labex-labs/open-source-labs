# Вычисление начальных точек (seeds) для k-means++

Мы будем использовать функцию `kmeans_plusplus` из библиотеки scikit-learn для вычисления начальных точек (seeds) для k-means++. Эта функция возвращает начальные центры кластеров, которые используются для кластеризации k-means. Мы вычислим 4 кластера с использованием k-means++.

```python
# Calculate seeds from k-means++
centers_init, indices = kmeans_plusplus(X, n_clusters=4, random_state=0)
```

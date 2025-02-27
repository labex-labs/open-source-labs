# Выполним Спектральную бикластеризацию

Далее выполним бикластеризацию с использованием алгоритма Спектральная бикластеризация. Этот алгоритм предполагает, что матрица данных имеет скрытую шахматную структуру.

```python
# Initialize and fit the Spectral Biclustering model
model_bi = SpectralBiclustering(n_clusters=(2, 3), random_state=0)
model_bi.fit(data)

# Get row and column cluster membership
row_clusters_bi = model_bi.row_labels_
column_clusters_bi = model_bi.column_labels_
```

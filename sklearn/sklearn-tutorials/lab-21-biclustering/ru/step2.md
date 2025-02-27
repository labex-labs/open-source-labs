# Выполним Спектральное кокластеризацию

Теперь выполним бикластеризацию с использованием алгоритма Спектральное кокластеризация. Этот алгоритм находит бикластеры с более высокими значениями по сравнению с другими строками и столбцами.

```python
# Initialize and fit the Spectral Co-Clustering model
model_co = SpectralCoclustering(n_clusters=3, random_state=0)
model_co.fit(data)

# Get row and column cluster membership
row_clusters_co = model_co.row_labels_
column_clusters_co = model_co.column_labels_
```

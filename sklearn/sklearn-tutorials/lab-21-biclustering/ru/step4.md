# Визуализируем результаты

Наконец, давайте визуализируем структуры бикластеров, полученные с использованием алгоритмов Спектральное кокластеризация и Спектральная бикластеризация.

```python
# Visualization for Spectral Co-Clustering
print("Spectral Co-Clustering:")
print("Row clusters:")
print(row_clusters_co)
print("Column clusters:")
print(column_clusters_co)

# Visualization for Spectral Biclustering
print("\nSpectral Biclustering:")
print("Row clusters:")
print(row_clusters_bi)
print("Column clusters:")
print(column_clusters_bi)
```

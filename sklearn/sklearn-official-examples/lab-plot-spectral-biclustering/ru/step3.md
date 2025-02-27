# Применение `SpectralBiclustering`

Мы обучаем модель и сравниваем полученные кластеры с истинными значениями. Обратите внимание, что при создании модели мы указываем такое же количество кластеров, которое мы использовали для создания датасета (`n_clusters = (4, 3)`), что способствует получению хорошего результата.

```python
from sklearn.cluster import SpectralBiclustering
from sklearn.metrics import consensus_score

model = SpectralBiclustering(n_clusters=n_clusters, method="log", random_state=0)
model.fit(data)

# Вычисление сходства двух наборов бикластеров
score = consensus_score(
    model.biclusters_, (rows[:, row_idx_shuffled], columns[:, col_idx_shuffled])
)
print(f"consensus score: {score:.1f}")
```

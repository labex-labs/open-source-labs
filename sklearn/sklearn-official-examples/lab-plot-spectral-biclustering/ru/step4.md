# Построение графиков результатов

Теперь мы переупорядочиваем данные в соответствии с метками строк и столбцов, присвоенными моделью `SpectralBiclustering`, в порядке возрастания и снова строим график. `row_labels_` имеет значения от 0 до 3, а `column_labels_` - от 0 до 2, что означает в сумме 4 кластера в каждой строке и 3 кластера в каждом столбце.

```python
# Переупорядочиваем сначала строки, а затем столбцы.
reordered_rows = data[np.argsort(model.row_labels_)]
reordered_data = reordered_rows[:, np.argsort(model.column_labels_)]

plt.matshow(reordered_data, cmap=plt.cm.Blues)
plt.title("После бикластеризации; переупорядочено для отображения бикластеров")
_ = plt.show()
```

В качестве последнего шага мы хотим показать связи между метками строк и столбцов, присвоенными моделью. Поэтому мы создаем сетку с использованием `numpy.outer`, которая берет отсортированные `row_labels_` и `column_labels_` и прибавляет 1 к каждому, чтобы метки начинались с 1 вместо 0 для лучшей визуализации.

```python
plt.matshow(
    np.outer(np.sort(model.row_labels_) + 1, np.sort(model.column_labels_) + 1),
    cmap=plt.cm.Blues,
)
plt.title("Шахматная структура переупорядоченных данных")
plt.show()
```

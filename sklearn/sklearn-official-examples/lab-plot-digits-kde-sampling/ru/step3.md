# Генерация новых выборок

Мы используем наилучший метод для отбора 44 новых точек из данных. Затем мы преобразуем новые данные обратно в исходные 64 измерения с использованием обратной матрицы PCA.

```python
# sample 44 new points from the data
new_data = kde.sample(44, random_state=0)
new_data = pca.inverse_transform(new_data)
```

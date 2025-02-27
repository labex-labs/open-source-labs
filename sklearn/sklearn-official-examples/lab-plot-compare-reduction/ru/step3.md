# Создаем объект GridSearchCV и подгоняем данные

Создадим объект `GridSearchCV` с использованием конвейера и сетки параметров, определенных на предыдущем этапе. Затем подгоним данные к этому объекту.

```python
grid = GridSearchCV(pipe, n_jobs=1, param_grid=param_grid)
grid.fit(X, y)
```

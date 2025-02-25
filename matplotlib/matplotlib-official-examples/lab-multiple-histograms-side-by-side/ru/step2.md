# Создаем примерные наборы данных

Далее мы создадим примерные наборы данных, которые будем использовать для наших гистограмм. Мы создадим три набора данных по 387 точкам данных каждый:

```python
np.random.seed(19680801)
number_of_data_points = 387
labels = ["A", "B", "C"]
data_sets = [np.random.normal(0, 1, number_of_data_points),
             np.random.normal(6, 1, number_of_data_points),
             np.random.normal(-3, 1, number_of_data_points)]
```

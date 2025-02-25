# Создание данных о дождях

Далее мы создадим данные о дождях. Мы создадим 50 капель дождя в случайных позициях, с случайными скоростями роста и случайными цветами.

```python
n_drops = 50
rain_drops = np.zeros(n_drops, dtype=[('position', float, (2,)),
                                      ('size',     float),
                                      ('growth',   float),
                                      ('color',    float, (4,))])

rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)
```

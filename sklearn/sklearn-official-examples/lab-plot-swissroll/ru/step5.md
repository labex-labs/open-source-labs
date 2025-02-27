# Создание набора данных Swiss-Hole

Мы создаем набор данных Swiss-Hole, добавив отверстие в набор данных Swiss Roll с использованием параметра `hole=True` в функции `make_swiss_roll()`.

```python
sh_points, sh_color = datasets.make_swiss_roll(n_samples=1500, hole=True, random_state=0)
```

# Создаем подграфики

Мы создадим фигуру, содержащую два подграфика, один с mathtext, а другой с usetex. Мы будем использовать метод `subplots()` для создания подграфиков.

```python
fig, axs = plt.subplots(1, 2, figsize=(2 * 3, 6.5))
```

# Создание фигуры и подграфиков

Следующим шагом является создание фигуры и подграфиков. Мы создадим фигуру с двумя рядом стоящими подграфиками с использованием функции `subplots`.

```python
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(7, 4))
```

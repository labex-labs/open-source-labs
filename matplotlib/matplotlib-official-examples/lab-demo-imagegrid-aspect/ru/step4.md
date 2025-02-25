# Задаем соотношение сторон

Мы зададим соотношение сторон ячеек в ImageGrid равным 2 с использованием функции `set_aspect()`.

```python
for i in [0, 1]:
    grid1[i].set_aspect(2)

for i in [1, 3]:
    grid2[i].set_aspect(2)
```

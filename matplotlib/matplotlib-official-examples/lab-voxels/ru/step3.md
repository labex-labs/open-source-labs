# Создание кубов и связи между ними

Теперь мы создадим два куба и связь между ними. Для этого мы определим три булевых массива, которые будут объединены в один булевый массив. Первые два массива определяют расположение кубов, а третий массив определяет расположение связи между ними.

```python
cube1 = (x < 3) & (y < 3) & (z < 3)
cube2 = (x >= 5) & (y >= 5) & (z >= 5)
link = abs(x - y) + abs(y - z) + abs(z - x) <= 2

voxelarray = cube1 | cube2 | link
```

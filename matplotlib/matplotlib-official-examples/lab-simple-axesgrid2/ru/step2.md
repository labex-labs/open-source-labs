# Создаем фигуру и ImageGrid

Далее мы создаем фигуру и ImageGrid с параметром `nrows_ncols`, чтобы определить количество строк и столбцов в сетке.

```python
fig = plt.figure(figsize=(5.5, 3.5))
grid = ImageGrid(fig, 111,  # аналогично subplot(111)
                 nrows_ncols=(1, 3),
                 axes_pad=0.1,
                 label_mode="L")
```

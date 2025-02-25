# Создаем ImageGrid

Мы создадим два ImageGrid для отображения наших изображений. Первый ImageGrid будет иметь две строки и два столбца, а второй ImageGrid также будет иметь две строки и два столбца.

```python
grid1 = ImageGrid(fig, 121, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
grid2 = ImageGrid(fig, 122, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
```

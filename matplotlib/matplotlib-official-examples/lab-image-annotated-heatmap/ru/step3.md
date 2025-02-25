# Применение функции

Теперь, когда у нас есть функции, мы можем использовать их для создания тепловой карты с аннотациями. Мы создаем новый набор данных, передаем дополнительные аргументы в `imshow`, используем целый формат для аннотаций и задаем некоторые цвета. Мы также скрываем диагональные элементы (которые все равны 1), используя `matplotlib.ticker.FuncFormatter`.

```python
data = np.random.randint(2, 100, size=(7, 7))
y = [f"Book {i}" for i in range(1, 8)]
x = [f"Store {i}" for i in list("ABCDEFG")]

fig, ax = plt.subplots()
im, _ = heatmap(data, y, x, ax=ax, vmin=0, cmap="magma_r", cbarlabel="weekly sold copies")
annotate_heatmap(im, valfmt="{x:d}", size=7, threshold=20, textcolors=("red", "white"))

def func(x, pos):
    return f"{x:.2f}".replace("0.", ".").replace("1.00", "")

annotate_heatmap(im, valfmt=matplotlib.ticker.FuncFormatter(func), size=7)
```

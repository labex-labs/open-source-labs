# Рисуем изображения текста на фигуре

После того, как мы преобразовали текст в RGBA-изображение, мы можем нарисовать его на фигуре с использованием `.Figure.figimage`.

```python
fig = plt.figure()
rgba1 = text_to_rgba(r"IQ: $\sigma_i=15$", color="blue", fontsize=20, dpi=200)
rgba2 = text_to_rgba(r"some other string", color="red", fontsize=20, dpi=200)

fig.figimage(rgba1, 100, 50)
fig.figimage(rgba2, 100, 150)

plt.show()
```

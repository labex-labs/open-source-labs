# Создаем BboxImage с текстом

Начнем с создания BboxImage с текстом. Создаем объект `text` с помощью метода `text()` и добавляем его в объект `ax1`. Затем создаем объект `BboxImage` с использованием метода `add_artist()`. Передаем метод `get_window_extent` объекта `text` в конструктор `BboxImage`, чтобы получить ограничивающую рамку для текста. Также передаем одномерный массив формы (1, 256) в параметр `data` конструктора `BboxImage`, чтобы создать изображение.

```python
fig, (ax1, ax2) = plt.subplots(ncols=2)

txt = ax1.text(0.5, 0.5, "test", size=30, ha="center", color="w")
ax1.add_artist(
    BboxImage(txt.get_window_extent, data=np.arange(256).reshape((1, -1))))
```

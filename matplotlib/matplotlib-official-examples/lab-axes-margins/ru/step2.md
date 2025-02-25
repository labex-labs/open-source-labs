# Прикрепленные края

Некоторые функции построения графиков в Matplotlib делают пределы осей "прикрепленными" или нечувствительными к методу `margins()`. Например, `imshow()` и `pcolor()` предполагают, что пользователь хочет, чтобы пределы были тесно вокруг пикселей, показанных на графике. Если такое поведение нежелательно, вам нужно установить `use_sticky_edges` в `False`. В этом шаге мы узнаем, как обойти прикрепленные края в Matplotlib.

```python
# создать сетку
y, x = np.mgrid[:5, 1:6]

# определить координаты полигона
poly_coords = [
    (0.25, 2.75), (3.25, 2.75),
    (2.25, 0.75), (0.25, 0.75)
]

# создать подграфики
fig, (ax1, ax2) = plt.subplots(ncols=2)

# использовать прикрепленные края для ax1 и отключить прикрепленные края для ax2
ax2.use_sticky_edges = False

# построить на обоих подграфиках
for ax, status in zip((ax1, ax2), ('Is', 'Is Not')):
    cells = ax.pcolor(x, y, x+y, cmap='inferno', shading='auto') # sticky
    ax.add_patch(
        Polygon(poly_coords, color='forestgreen', alpha=0.5)
    ) # not sticky
    ax.margins(x=0.1, y=0.05)
    ax.set_aspect('equal')
    ax.set_title(f'{status} Sticky')

plt.show()
```

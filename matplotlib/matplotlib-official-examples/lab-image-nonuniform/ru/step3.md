# Создание подграфиков и NonUniformImage

Теперь мы создаем подграфики и добавляем в каждый из них NonUniformImage. Мы создадим четыре подграфика, два с интерполяцией 'nearest' и два с интерполяцией 'bilinear'. Аргумент ключевого слова interpolation определяет тип интерполяции, используемый для отображения изображения.

```python
# Создание подграфиков
fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')
fig.suptitle('NonUniformImage class', fontsize='large')

# Интерполяция nearest
ax = axs[0, 0]
im = NonUniformImage(ax, interpolation='nearest', extent=(-4, 4, -4, 4), cmap=cm.Purples)
im.set_data(x, y, z)
ax.add_image(im)
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_title('nearest')

ax = axs[0, 1]
im = NonUniformImage(ax, interpolation='nearest', extent=(-64, 64, -4, 4), cmap=cm.Purples)
im.set_data(x2, y, z)
ax.add_image(im)
ax.set_xlim(-64, 64)
ax.set_ylim(-4, 4)
ax.set_title('nearest')

# Интерполяция bilinear
ax = axs[1, 0]
im = NonUniformImage(ax, interpolation='bilinear', extent=(-4, 4, -4, 4), cmap=cm.Purples)
im.set_data(x, y, z)
ax.add_image(im)
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_title('bilinear')

ax = axs[1, 1]
im = NonUniformImage(ax, interpolation='bilinear', extent=(-64, 64, -4, 4), cmap=cm.Purples)
im.set_data(x2, y, z)
ax.add_image(im)
ax.set_xlim(-64, 64)
ax.set_ylim(-4, 4)
ax.set_title('bilinear')

plt.show()
```

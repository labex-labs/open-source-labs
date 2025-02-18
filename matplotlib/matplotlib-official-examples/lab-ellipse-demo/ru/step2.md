# Рисование отдельных эллипсов

В этом примере мы нарисуем множество эллипсов со случайными размерами, положениями и цветами. Каждый эллипс будет экземпляром класса `Ellipse`.

```python
# Фиксация случайного состояния для воспроизводимости
np.random.seed(19680801)

# Количество эллипсов для рисования
NUM = 250

# Генерация эллипсов
ells = [Ellipse(xy=np.random.rand(2) * 10,
                width=np.random.rand(), height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]

# Создание графика и установка соотношения сторон как 'equal'
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# Добавление каждого эллипса на график
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(np.random.rand())
    e.set_facecolor(np.random.rand(3))

# Установка пределов по осям x и y графика
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Отображение графика
plt.show()
```

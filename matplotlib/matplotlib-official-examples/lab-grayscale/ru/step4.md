# Определение функции примера изображения и участка

Мы определяем функцию `image_and_patch_example`, которая принимает объект оси в качестве входных данных, отображает случайное изображение и добавляет участок на график.

```python
def image_and_patch_example(ax):
    ax.imshow(np.random.random(size=(20, 20)), interpolation='none')
    c = plt.Circle((5, 5), radius=5, label='patch')
    ax.add_patch(c)
```

# Простая подборка, линии, прямоугольники и текст

Начнем с включения простой подборки, установив свойство "picker" для художника. Это позволит художнику сгенерировать событие подбора, если событие мыши происходит над художником. Создадим простую диаграмму, содержащую линию, прямоугольник и текст, и применим подборку для каждого из этих художников.

```python
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.set_title('click on points, rectangles or text', picker=True)
ax1.set_ylabel('ylabel', picker=True, bbox=dict(facecolor='red'))
line, = ax1.plot(rand(100), 'o', picker=True, pickradius=5)

# Выберите прямоугольник.
ax2.bar(range(10), rand(10), picker=True)
for label in ax2.get_xticklabels():  # Сделайте метки делений по оси x доступными для подбора.
    label.set_picker(True)
```

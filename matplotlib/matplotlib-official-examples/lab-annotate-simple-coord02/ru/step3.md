# Добавление стрелковой аннотации

Стрелочки можно использовать, чтобы указать на определенные особенности или тенденции на графике. В этом шаге мы добавим стрелку на график, которая будет указывать на максимальное значение.

```python
# Find the maximum value
y = [0, 1, 4, 9, 16]
max_index = y.index(max(y))
xmax = max_index
ymax = y[max_index]

# Add arrow annotation
ax.annotate('Maximum Value', xy=(xmax, ymax), xytext=(xmax, ymax + 5),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```

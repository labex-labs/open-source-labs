# Добавляем стрелковую аннотацию с единицами измерения для xy и текста

В этом шаге мы добавим стрелковую аннотацию на график с использованием функции `annotate()`. Мы укажем позицию стрелки, текст, который будет отображаться, и свойства стрелки. Также мы укажем единицы измерения для позиции и текста.

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8*cm, 0.95*cm), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```

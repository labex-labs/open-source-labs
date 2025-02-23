# Добавляем стрелковую аннотацию с смешанными единицами измерения

В этом шаге мы добавим еще одну стрелковую аннотацию на график с использованием функции `annotate()`. Мы укажем позицию стрелки, текст, который будет отображаться, и свойства стрелки. Также мы смешаем единицы измерения для позиции и используем долю оси для текста.

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```

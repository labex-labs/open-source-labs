# Добавление текста на график

Мы можем добавить текст на график с использованием функции `ax.text()`. Эта функция принимает три аргумента: координату x, координату y и строку с текстом. Мы можем настроить стиль текста с использованием аргументов `style`, `bbox` и `fontsize`.

```python
ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor':'red', 'alpha': 0.5, 'pad': 10})

ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

ax.text(3, 2, 'Unicode: Institut f\374r Festk\366rperphysik')

ax.text(0.95, 0.01, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)
```

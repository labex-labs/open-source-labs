# Управление расположением и стилем текста

Мы также можем контролировать расположение и стиль текста в нашем графике Matplotlib. Попробуйте добавить следующий код в свой скрипт:

```python
plt.text(2, 8, "Top Left", fontsize=12, color='red')
plt.text(8, 8, "Top Right", fontsize=12, color='blue')
plt.text(2, 2, "Bottom Left", fontsize=12, color='green')
plt.text(8, 2, "Bottom Right", fontsize=12, color='purple')
```

Это добавит четыре текстовых элемента к нашему графику, каждый с разным цветом, размером шрифта и позицией.

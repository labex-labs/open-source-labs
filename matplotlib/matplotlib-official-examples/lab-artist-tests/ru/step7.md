# Создание графического элемента текста

Далее вы создадите графический элемент текста с использованием класса `Text` из `matplotlib.text`. Вы можете указать координаты x и y, метку текста, горизонтальное и вертикальное выравнивание и объект оси в качестве аргументов.

```python
t = text.Text(3, 2.5, 'text label', ha='left', va='bottom', axes=ax)
```

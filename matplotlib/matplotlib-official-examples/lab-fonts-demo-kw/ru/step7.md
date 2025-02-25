# Показать жирный курсив

В качестве бонусного материала мы также можем отобразить текст в стиле как жирный, так и курсив. Мы будем использовать метод `fig.text()` для отображения текста с соответствующим стилем, весом и размером.

```python
fig.text(0.3, 0.1, 'bold italic',
         style='italic', weight='bold', size='x-small', **alignment)
fig.text(0.3, 0.2, 'bold italic',
         style='italic', weight='bold', size='medium', **alignment)
fig.text(0.3, 0.3, 'bold italic',
         style='italic', weight='bold', size='x-large', **alignment)
```

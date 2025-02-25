# Добавление текста на график

Мы можем добавить текст на график с использованием функции `text`. Мы можем указать позицию, вращение, горизонтальное и вертикальное выравнивание и выравнивание по нескольким строкам текста.

```python
ax0.text(2, 7, 'this is\nyet another test',
         rotation=45,
         horizontalalignment='center',
         verticalalignment='top',
         multialignment='center')
```

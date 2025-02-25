# Добавляем метки и форматирование

Мы добавим метки к участкам диаграммы Санки с использованием атрибута `text` каждого участка. Также отформатируем текст, сделав его жирным и увеличив размер шрифта.

```python
diagrams = sankey.finish()
for diagram in diagrams:
    diagram.text.set_fontweight('bold')
    diagram.text.set_fontsize('10')
    for text in diagram.texts:
        text.set_fontsize('10')
```

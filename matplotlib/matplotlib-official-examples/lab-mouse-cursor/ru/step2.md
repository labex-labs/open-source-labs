# Создаем фигуру и назначаем альтернативные курсоры

Далее мы создаем фигуру и назначаем альтернативные курсоры для каждого подграфика с использованием цикла. Также добавляем текст в каждый подграфик, чтобы указать используемый курсор.

```python
fig, axs = plt.subplots(len(Cursors), figsize=(6, len(Cursors) + 0.5), gridspec_kw={'hspace': 0})
fig.suptitle('Hover over an Axes to see alternate Cursors')

for cursor, ax in zip(Cursors, axs):
    ax.cursor_to_use = cursor
    ax.text(0.5, 0.5, cursor.name,
            horizontalalignment='center', verticalalignment='center')
    ax.set(xticks=[], yticks=[])
```

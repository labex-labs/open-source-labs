# Criar uma figura e definir cursores alternativos

Em seguida, criamos uma figura e definimos os cursores alternativos para cada subplot usando um loop. Também adicionamos texto a cada subplot para indicar o cursor que está sendo usado.

```python
fig, axs = plt.subplots(len(Cursors), figsize=(6, len(Cursors) + 0.5), gridspec_kw={'hspace': 0})
fig.suptitle('Passe o mouse sobre um Axes para ver os Cursors alternativos')

for cursor, ax in zip(Cursors, axs):
    ax.cursor_to_use = cursor
    ax.text(0.5, 0.5, cursor.name,
            horizontalalignment='center', verticalalignment='center')
    ax.set(xticks=[], yticks=[])
```

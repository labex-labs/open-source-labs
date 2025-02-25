# Créez une figure et définissez des curseurs alternatifs

Ensuite, nous créons une figure et définissons les curseurs alternatifs pour chaque sous-graphique en utilisant une boucle. Nous ajoutons également du texte à chaque sous-graphique pour indiquer le curseur utilisé.

```python
fig, axs = plt.subplots(len(Cursors), figsize=(6, len(Cursors) + 0.5), gridspec_kw={'hspace': 0})
fig.suptitle('Survolez un axe pour voir les curseurs alternatifs')

for cursor, ax in zip(Cursors, axs):
    ax.cursor_to_use = cursor
    ax.text(0.5, 0.5, cursor.name,
            horizontalalignment='center', verticalalignment='center')
    ax.set(xticks=[], yticks=[])
```

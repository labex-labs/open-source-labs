# Définissez le formatteur et le localisateur de graduations

Nous définissons le formatteur d'étiquettes de graduation de l'axe x sur la fonction de formatage créée à l'étape 5 en utilisant la méthode `set_major_formatter()`. Nous définissons également le localisateur d'étiquettes de graduation de l'axe x sur `MaxNLocator(integer=True)` pour vous assurer que les valeurs des graduations prennent des valeurs entières.

```python
ax.xaxis.set_major_formatter(format_fn)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
```

# Personnaliser les sous-figures

Vous pouvez personnaliser les sous-figures à l'aide des diverses fonctions disponibles dans Matplotlib. Par exemple, vous pouvez définir le titre et les étiquettes des axes à l'aide de `set_title()` et `set_xlabel()`/`set_ylabel()`.

```python
ax1.set_title('Sous-figure 1')
ax1.set_xlabel('Étiquette de X')
ax1.set_ylabel('Étiquette de Y')

ax2.set_title('Sous-figure 2')
ax2.set_xlabel('Étiquette de X')
ax2.set_ylabel('Étiquette de Y')
```

Cela définira les titres et les étiquettes des axes pour chaque sous-figure.

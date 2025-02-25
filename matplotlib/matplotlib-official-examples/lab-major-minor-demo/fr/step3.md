# Définissez les localisateurs principaux et mineurs

```python
# Définissez le localisateur principal
ax.xaxis.set_major_locator(MultipleLocator(20))
# Définissez le formatteur principal
ax.xaxis.set_major_formatter('{x:.0f}')
# Définissez le localisateur mineur
ax.xaxis.set_minor_locator(MultipleLocator(5))
```

Ici, nous définissons le localisateur principal pour placer les étiquettes graduées à des multiples de 20, définissons le formatteur principal pour étiqueter les étiquettes graduées principales avec le format ".0f", et définissons le localisateur mineur pour placer les étiquettes graduées à des multiples de 5.

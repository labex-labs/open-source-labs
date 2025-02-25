# Establece los localizadores principales y secundarios

```python
# Establece el localizador principal
ax.xaxis.set_major_locator(MultipleLocator(20))
# Establece el formateador principal
ax.xaxis.set_major_formatter('{x:.0f}')
# Establece el localizador secundario
ax.xaxis.set_minor_locator(MultipleLocator(5))
```

Aquí, establecemos el localizador principal para colocar marcas de graduación en múltiplos de 20, establecemos el formateador principal para etiquetar las marcas principales con el formato ".0f" y establecemos el localizador secundario para colocar marcas de graduación en múltiplos de 5.

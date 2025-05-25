# Definir os localizadores principais e secundários

```python
# Set the major locator
ax.xaxis.set_major_locator(MultipleLocator(20))
# Set the major formatter
ax.xaxis.set_major_formatter('{x:.0f}')
# Set the minor locator
ax.xaxis.set_minor_locator(MultipleLocator(5))
```

Aqui, definimos o localizador principal para colocar as marcas em múltiplos de 20, definimos o formatador principal para rotular as marcas principais com a formatação ".0f" e definimos o localizador secundário para colocar as marcas em múltiplos de 5.

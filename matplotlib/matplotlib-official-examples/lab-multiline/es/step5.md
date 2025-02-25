# Agregando texto a la gráfica

Podemos agregar texto a la gráfica utilizando la función `text`. Podemos especificar la posición, la rotación, la alineación horizontal y vertical, y la multialineación del texto.

```python
ax0.text(2, 7, 'this is\nyet another test',
         rotation=45,
         horizontalalignment='center',
         verticalalignment='top',
         multialignment='center')
```

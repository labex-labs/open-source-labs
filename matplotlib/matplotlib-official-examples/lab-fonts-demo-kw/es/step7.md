# Mostrar negrita e itálica

Como bono, también podemos mostrar texto con estilos de negrita e itálica al mismo tiempo. Utilizaremos el método `fig.text()` para mostrar el texto con el estilo, peso y tamaño adecuados.

```python
fig.text(0.3, 0.1, 'bold italic',
         style='italic', weight='bold', size='x-small', **alignment)
fig.text(0.3, 0.2, 'bold italic',
         style='italic', weight='bold', size='medium', **alignment)
fig.text(0.3, 0.3, 'bold italic',
         style='italic', weight='bold', size='x-large', **alignment)
```

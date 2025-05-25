# Mostrar negrito itálico

Como um bônus, também podemos exibir texto com estilos negrito e itálico. Usaremos o método `fig.text()` para exibir o texto com o estilo, peso e tamanho apropriados.

```python
fig.text(0.3, 0.1, 'bold italic',
         style='italic', weight='bold', size='x-small', **alignment)
fig.text(0.3, 0.2, 'bold italic',
         style='italic', weight='bold', size='medium', **alignment)
fig.text(0.3, 0.3, 'bold italic',
         style='italic', weight='bold', size='x-large', **alignment)
```

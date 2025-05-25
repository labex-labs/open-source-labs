# Mostrar estilos de fonte

Agora, exibiremos os diferentes estilos de fonte disponíveis no Matplotlib. Usaremos o método `fig.text()` para exibir cada estilo de fonte, com o nome do estilo como texto e o estilo de fonte correspondente como um argumento de palavra-chave.

```python
fig.text(0.3, 0.9, 'style', **alignment)
styles = ['normal', 'italic', 'oblique']
for k, style in enumerate(styles):
    fig.text(0.3, yp[k], style, family='sans-serif', style=style, **alignment)
```

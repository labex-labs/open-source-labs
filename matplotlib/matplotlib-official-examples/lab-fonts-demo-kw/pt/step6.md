# Mostrar tamanhos de fonte

Finalmente, exibiremos os diferentes tamanhos de fonte disponíveis no Matplotlib. Usaremos o método `fig.text()` para exibir cada tamanho de fonte, com o nome do tamanho como texto e o tamanho de fonte correspondente como um argumento de palavra-chave.

```python
fig.text(0.9, 0.9, 'size', **alignment)
sizes = [
    'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']
for k, size in enumerate(sizes):
    fig.text(0.9, yp[k], size, size=size, **alignment)
```

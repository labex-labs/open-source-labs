# Mostrar famílias de fontes

Em seguida, exibiremos as diferentes famílias de fontes disponíveis no Matplotlib. Usaremos o método `fig.text()` para exibir cada família de fonte, com o nome da família como texto e a família de fonte correspondente como um argumento de palavra-chave.

```python
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

fig.text(0.1, 0.9, 'family', size='large', **alignment)
families = ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']
for k, family in enumerate(families):
    fig.text(0.1, yp[k], family, family=family, **alignment)
```

# Mostrar variantes de fonte

Em seguida, exibiremos as diferentes variantes de fonte disponíveis no Matplotlib. Usaremos o método `fig.text()` para exibir cada variante de fonte, com o nome da variante como texto e a variante de fonte correspondente como um argumento de palavra-chave.

```python
fig.text(0.5, 0.9, 'variant', **alignment)
variants = ['normal', 'small-caps']
for k, variant in enumerate(variants):
    fig.text(0.5, yp[k], variant, family='serif', variant=variant, **alignment)
```

# Mostrar pesos de fonte

Agora, exibiremos os diferentes pesos de fonte disponíveis no Matplotlib. Usaremos o método `fig.text()` para exibir cada peso de fonte, com o nome do peso como texto e o peso de fonte correspondente como um argumento de palavra-chave.

```python
fig.text(0.7, 0.9, 'weight', **alignment)
weights = ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
for k, weight in enumerate(weights):
    fig.text(0.7, yp[k], weight, weight=weight, **alignment)
```

# Criar a Figura e o `GridSpec` Externo

O próximo passo é criar uma figura e um `gridspec` externo. Neste exemplo, criaremos um `gridspec` de 1 por 2.

```python
fig = plt.figure()
gs0 = gridspec.GridSpec(1, 2, figure=fig)
```

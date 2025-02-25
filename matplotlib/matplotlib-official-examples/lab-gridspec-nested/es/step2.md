# Crear la figura y el gridspec externo

El siguiente paso es crear una figura y un gridspec externo. En este ejemplo, crearemos un gridspec de 1 por 2.

```python
fig = plt.figure()
gs0 = gridspec.GridSpec(1, 2, figure=fig)
```

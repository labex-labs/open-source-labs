# Criar uma figura e adicionar eixos hospedeiros

Criamos uma figura usando o método `plt.figure()` e adicionamos um eixo hospedeiro usando o método `fig.add_axes()`. O eixo hospedeiro compartilha a escala x com os eixos parasitas.

```python
fig = plt.figure()
host = fig.add_axes([0.15, 0.1, 0.65, 0.8], axes_class=HostAxes)
```

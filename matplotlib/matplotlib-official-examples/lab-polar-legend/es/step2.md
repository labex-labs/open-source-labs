# Crear una figura y un subgráfico

A continuación, necesitamos crear una figura y un subgráfico para nuestro gráfico. Usaremos el parámetro `projection` de `add_subplot` para crear un gráfico polar.

```python
fig = plt.figure()
ax = fig.add_subplot(projection="polar", facecolor="lightgoldenrodyellow")
```

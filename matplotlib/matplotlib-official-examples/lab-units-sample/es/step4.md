# Crear la gráfica

Crea una cuadrícula de subgráficos de 2x2 utilizando la función `subplots`. Luego, utiliza la función `plot` para graficar los datos en cada subgráfico.

```python
fig, axs = plt.subplots(2, 2, layout='constrained')

axs[0, 0].plot(cms, cms)

axs[0, 1].plot(cms, cms, xunits=cm, yunits=inch)

axs[1, 0].plot(cms, cms, xunits=inch, yunits=cm)
axs[1, 0].set_xlim(-1, 4)  # los escalares se interpretan en las unidades actuales

axs[1, 1].plot(cms, cms, xunits=inch, yunits=inch)
axs[1, 1].set_xlim(3*cm, 6*cm)  # los cm se convierten a pulgadas
```

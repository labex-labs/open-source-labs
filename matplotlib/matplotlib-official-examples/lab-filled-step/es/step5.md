# Configurar ciclos de estilo

Configuraremos ciclos de estilo para los histogramas utilizando `cycler`. Crearemos tres ciclos de estilo: uno para el color de fondo, uno para la etiqueta y uno para el patrón de sombreado.

```python
color_cycle = cycler(facecolor=plt.rcParams['axes.prop_cycle'][:4])
label_cycle = cycler(label=[f'set {n}' for n in range(4)])
hatch_cycle = cycler(hatch=['/', '*', '+', '|'])
```

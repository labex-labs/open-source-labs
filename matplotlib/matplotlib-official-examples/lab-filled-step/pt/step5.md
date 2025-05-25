# Configurar ciclos de estilo

Configuraremos ciclos de estilo para os histogramas usando `cycler`. Criaremos três ciclos de estilo: um para a cor de preenchimento (facecolor), um para o rótulo (label) e um para o padrão de hachura (hatch).

```python
color_cycle = cycler(facecolor=plt.rcParams['axes.prop_cycle'][:4])
label_cycle = cycler(label=[f'set {n}' for n in range(4)])
hatch_cycle = cycler(hatch=['/', '*', '+', '|'])
```

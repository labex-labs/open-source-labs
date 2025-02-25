# Crear el gráfico

En este paso, crearemos el gráfico. Utilizaremos el método `fig.text()` para agregar texto al gráfico. Iteraremos sobre una lista de fuentes y el texto correspondiente, utilizando la función `zip()` para emparejarlos. Estableceremos el parámetro `usetex` en `True` para habilitar el modo usetex.

```python
fig = plt.figure()
for y, font, text in zip(
    range(5),
    ['ptmr8r', 'ptmri8r', 'ptmro8r', 'ptmr8rn', 'ptmrr8re'],
    [f'Nimbus Roman No9 L {x}'
     for x in ['', 'Italics (real italics for comparison)',
               '(slanted)', '(condensed)', '(extended)']],
):
    fig.text(.1, 1 - (y + 1) / 6, setfont(font) + text, usetex=True)

fig.suptitle('Usetex font effects')
plt.show()
```

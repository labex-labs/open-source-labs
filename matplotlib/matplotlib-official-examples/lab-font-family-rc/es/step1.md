# Elegir la fuente sans-serif predeterminada

La familia de fuentes predeterminada en Matplotlib es sans-serif. Podemos elegir utilizar la familia de fuentes predeterminada estableciendo el parámetro `font.family` en `'sans-serif'`. Para hacer esto, podemos utilizar el siguiente código:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
```

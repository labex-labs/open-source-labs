# Elegir la fuente monospace predeterminada

La fuente monospace predeterminada en Matplotlib está determinada por el sistema operativo. Podemos elegir utilizar la fuente monospace predeterminada estableciendo el parámetro `font.family` en `'monospace'`. Para hacer esto, podemos utilizar el siguiente código:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
```

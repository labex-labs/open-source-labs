# Elegir una fuente monospace específica

Si queremos utilizar una fuente monospace específica, podemos establecer el parámetro `font.monospace` en una lista de nombres de fuentes. Matplotlib intentará utilizar la primera fuente de la lista que esté disponible en el sistema del usuario. Para hacer esto, podemos utilizar el siguiente código:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
plt.rcParams["font.monospace"] = ["FreeMono"]
```

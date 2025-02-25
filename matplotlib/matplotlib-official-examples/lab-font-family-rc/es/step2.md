# Elegir una fuente sans-serif específica

Si queremos utilizar una fuente sans-serif específica, podemos establecer el parámetro `font.sans-serif` en una lista de nombres de fuentes. Matplotlib intentará utilizar la primera fuente de la lista que esté disponible en el sistema del usuario. Para hacer esto, podemos utilizar el siguiente código:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Nimbus Sans"]
```

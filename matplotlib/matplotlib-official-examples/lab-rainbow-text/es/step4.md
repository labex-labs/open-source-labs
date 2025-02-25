# Mostrar la gráfica

Una vez que haya creado y personalizado todos los objetos de texto, puede mostrar la gráfica utilizando `plt.show()`. El siguiente bloque de código muestra el código completo para la gráfica.

```python
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 20
ax = plt.figure().add_subplot(xticks=[], yticks=[])

# La primera palabra, creada con text().
text = ax.text(.1,.5, "Matplotlib", color="red")
# Palabras siguientes, posicionadas con annotate(), con respecto a la anterior.
text = ax.annotate(
    " dice,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="oro", weight="bold")  # propiedades personalizadas
text = ax.annotate(
    " hola", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="verde", style="italic")  # propiedades personalizadas
text = ax.annotate(
    " mundo!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="azul", family="serif")  # propiedades personalizadas

plt.show()
```

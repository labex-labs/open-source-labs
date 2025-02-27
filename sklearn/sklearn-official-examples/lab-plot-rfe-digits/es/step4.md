# Visualizar las clasificaciones de las características

Finalmente, graficaremos las clasificaciones de las características utilizando la biblioteca Matplotlib. Usaremos la función `matshow()` para mostrar las clasificaciones como una imagen. También agregaremos una barra de colores y un título al gráfico.

```python
import matplotlib.pyplot as plt

plt.matshow(ranking, cmap=plt.cm.Blues)
plt.colorbar()
plt.title("Ranking of pixels with RFE")
plt.show()
```

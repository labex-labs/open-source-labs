# Evaluar la importancia de las características

Evaluamos la importancia de las características basada en la disminución media de la impureza (MDI). Las importancias de las características se proporcionan por el atributo ajustado `feature_importances_` y se calculan como la media y la desviación estándar de la acumulación de la disminución de la impureza dentro de cada árbol.

```python
import time
import matplotlib.pyplot as plt

start_time = time.time()
img_shape = data.images[0].shape
importances = forest.feature_importances_
elapsed_time = time.time() - start_time

print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")
imp_reshaped = importances.reshape(img_shape)
plt.matshow(imp_reshaped, cmap=plt.cm.hot)
plt.title("Pixel importances using impurity values")
plt.colorbar()
plt.show()
```

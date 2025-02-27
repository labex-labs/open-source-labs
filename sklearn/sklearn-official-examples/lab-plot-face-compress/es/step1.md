# Cargar y mostrar la imagen original

Comenzaremos cargando la imagen de la cara de un mapache desde Scipy. Mostraremos la imagen y comprobaremos su forma, tipo de datos y uso de memoria.

```python
from scipy.misc import face
import matplotlib.pyplot as plt

raccoon_face = face(gray=True)

print(f"La dimensión de la imagen es {raccoon_face.shape}")
print(f"Los datos utilizados para codificar la imagen son del tipo {raccoon_face.dtype}")
print(f"El número de bytes ocupados en la RAM es {raccoon_face.nbytes}")

fig, ax = plt.subplots(ncols=2, figsize=(12, 4))
ax[0].imshow(raccoon_face, cmap=plt.cm.gray)
ax[0].axis("off")
ax[0].set_title("Imagen original")
ax[1].hist(raccoon_face.ravel(), bins=256)
ax[1].set_xlabel("Valor del píxel")
ax[1].set_ylabel("Conteo de píxeles")
ax[1].set_title("Distribución de los valores de los píxeles")
_ = fig.suptitle("Imagen original de la cara de un mapache")
```

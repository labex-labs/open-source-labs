# Charger et afficher l'image originale

Nous commencerons par charger l'image du visage de raton laveur à partir de Scipy. Nous afficherons l'image et vérifierons sa forme, son type de données et son utilisation mémoire.

```python
from scipy.misc import face
import matplotlib.pyplot as plt

raccoon_face = face(gray=True)

print(f"La dimension de l'image est {raccoon_face.shape}")
print(f"Les données utilisées pour encoder l'image sont de type {raccoon_face.dtype}")
print(f"Le nombre d'octets occupés en RAM est {raccoon_face.nbytes}")

fig, ax = plt.subplots(ncols=2, figsize=(12, 4))
ax[0].imshow(raccoon_face, cmap=plt.cm.gray)
ax[0].axis("off")
ax[0].set_title("Image originale")
ax[1].hist(raccoon_face.ravel(), bins=256)
ax[1].set_xlabel("Valeur du pixel")
ax[1].set_ylabel("Nombre de pixels")
ax[1].set_title("Distribution des valeurs des pixels")
_ = fig.suptitle("Image originale du visage d'un raton laveur")
```

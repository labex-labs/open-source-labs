# Quantification vectorielle à l'aide de KBinsDiscretizer

Nous allons maintenant utiliser KBinsDiscretizer pour effectuer une quantification vectorielle sur l'image du visage de raton laveur. Nous utiliserons 8 niveaux de gris pour représenter l'image, ce qui peut être compressé pour n'utiliser que 3 bits par pixel. Nous utiliserons les stratégies d'échantillonnage uniforme et de regroupement k-moyennes pour mapper les valeurs de pixel aux 8 niveaux de gris.

#### Stratégie d'échantillonnage uniforme

Nous utiliserons tout d'abord la stratégie d'échantillonnage uniforme pour mapper les valeurs de pixel aux 8 niveaux de gris.

```python
from sklearn.preprocessing import KBinsDiscretizer

n_bins = 8
encoder = KBinsDiscretizer(
    n_bins=n_bins, encode="ordinal", strategy="uniform", random_state=0
)
compressed_raccoon_uniform = encoder.fit_transform(raccoon_face.reshape(-1, 1)).reshape(
    raccoon_face.shape
)

fig, ax = plt.subplots(ncols=2, figsize=(12, 4))
ax[0].imshow(compressed_raccoon_uniform, cmap=plt.cm.gray)
ax[0].axis("off")
ax[0].set_title("Echantillonnage uniforme")
ax[1].hist(compressed_raccoon_uniform.ravel(), bins=256)
ax[1].set_xlabel("Valeur du pixel")
ax[1].set_ylabel("Nombre de pixels")
ax[1].set_title("Distribution des valeurs des pixels")
_ = fig.suptitle("Visage de raton laveur compressé avec 3 bits et une stratégie uniforme")
```

#### Stratégie de regroupement k-moyennes

Nous allons maintenant utiliser la stratégie de regroupement k-moyennes pour mapper les valeurs de pixel aux 8 niveaux de gris.

```python
encoder = KBinsDiscretizer(
    n_bins=n_bins, encode="ordinal", strategy="kmeans", random_state=0
)
compressed_raccoon_kmeans = encoder.fit_transform(raccoon_face.reshape(-1, 1)).reshape(
    raccoon_face.shape
)

fig, ax = plt.subplots(ncols=2, figsize=(12, 4))
ax[0].imshow(compressed_raccoon_kmeans, cmap=plt.cm.gray)
ax[0].axis("off")
ax[0].set_title("Regroupement k-moyennes")
ax[1].hist(compressed_raccoon_kmeans.ravel(), bins=256)
ax[1].set_xlabel("Valeur du pixel")
ax[1].set_ylabel("Nombre de pixels")
ax[1].set_title("Distribution des valeurs des pixels")
_ = fig.suptitle("Visage de raton laveur compressé avec 3 bits et une stratégie k-moyennes")
```

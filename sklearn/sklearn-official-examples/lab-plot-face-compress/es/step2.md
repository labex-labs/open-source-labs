# Cuantización vectorial utilizando KBinsDiscretizer

Ahora utilizaremos KBinsDiscretizer para realizar la cuantización vectorial en la imagen de la cara de un mapache. Utilizaremos 8 niveles de gris para representar la imagen, lo que se puede comprimir para utilizar solo 3 bits por píxel. Utilizaremos las estrategias de clustering uniforme y k-medias para mapear los valores de píxeles a los 8 niveles de gris.

#### Estrategia de muestreo uniforme

Primero utilizaremos la estrategia de muestreo uniforme para mapear los valores de píxeles a los 8 niveles de gris.

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
ax[0].set_title("Muestreo uniforme")
ax[1].hist(compressed_raccoon_uniform.ravel(), bins=256)
ax[1].set_xlabel("Valor del píxel")
ax[1].set_ylabel("Conteo de píxeles")
ax[1].set_title("Distribución de los valores de los píxeles")
_ = fig.suptitle("Cara de mapache comprimida utilizando 3 bits y una estrategia uniforme")
```

#### Estrategia de clustering k-medias

Ahora utilizaremos la estrategia de clustering k-medias para mapear los valores de píxeles a los 8 niveles de gris.

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
ax[0].set_title("Clustering k-medias")
ax[1].hist(compressed_raccoon_kmeans.ravel(), bins=256)
ax[1].set_xlabel("Valor del píxel")
ax[1].set_ylabel("Conteo de píxeles")
ax[1].set_title("Distribución de los valores de los píxeles")
_ = fig.suptitle("Cara de mapache comprimida utilizando 3 bits y una estrategia de k-medias")
```

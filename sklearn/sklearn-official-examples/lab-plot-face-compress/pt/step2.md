# Quantização Vetorial usando KBinsDiscretizer

Agora usaremos o KBinsDiscretizer para realizar a quantização vetorial na imagem do rosto do guaxinim. Usaremos 8 níveis de cinza para representar a imagem, o que pode ser comprimido para usar apenas 3 bits por pixel. Usaremos as estratégias de agrupamento uniforme e k-means para mapear os valores de pixel para os 8 níveis de cinza.

#### Estratégia de Amostragem Uniforme

Primeiro, usaremos a estratégia de amostragem uniforme para mapear os valores de pixel para os 8 níveis de cinza.

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
ax[0].set_title("Amostragem Uniforme")
ax[1].hist(compressed_raccoon_uniform.ravel(), bins=256)
ax[1].set_xlabel("Valor do Pixel")
ax[1].set_ylabel("Contagem de Pixels")
ax[1].set_title("Distribuição dos valores dos pixels")
_ = fig.suptitle("Rosto de guaxinim comprimido usando 3 bits e uma estratégia uniforme")
```

#### Estratégia de Agrupamento K-means

Agora usaremos a estratégia de agrupamento k-means para mapear os valores de pixel para os 8 níveis de cinza.

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
ax[0].set_title("Agrupamento K-means")
ax[1].hist(compressed_raccoon_kmeans.ravel(), bins=256)
ax[1].set_xlabel("Valor do Pixel")
ax[1].set_ylabel("Contagem de Pixels")
ax[1].set_title("Distribuição dos valores dos pixels")
_ = fig.suptitle("Rosto de guaxinim comprimido usando 3 bits e uma estratégia K-means")
```

# Vektorisierung mit KBinsDiscretizer

Wir werden nun KBinsDiscretizer verwenden, um die Vektorisierung auf dem Waschbärenbild durchzuführen. Wir werden 8 Graustufen verwenden, um das Bild zu repräsentieren, was auf nur 3 Bits pro Pixel komprimiert werden kann. Wir werden die einheitlichen und k-Means-Clustering-Strategien verwenden, um die Pixelwerte auf die 8 Graustufen zuzuordnen.

#### Einheitliche Stichprobenstrategie

Wir werden zunächst die einheitliche Stichprobenstrategie verwenden, um die Pixelwerte auf die 8 Graustufen zuzuordnen.

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
ax[0].set_title("Einheitliche Stichprobe")
ax[1].hist(compressed_raccoon_uniform.ravel(), bins=256)
ax[1].set_xlabel("Pixelwert")
ax[1].set_ylabel("Anzahl der Pixel")
ax[1].set_title("Verteilung der Pixelwerte")
_ = fig.suptitle("Waschbärenbild, komprimiert mit 3 Bits und einer einheitlichen Strategie")
```

#### K-Means-Clustering-Strategie

Wir werden nun die k-Means-Clustering-Strategie verwenden, um die Pixelwerte auf die 8 Graustufen zuzuordnen.

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
ax[0].set_title("K-Means-Clustering")
ax[1].hist(compressed_raccoon_kmeans.ravel(), bins=256)
ax[1].set_xlabel("Pixelwert")
ax[1].set_ylabel("Anzahl der Pixel")
ax[1].set_title("Verteilung der Pixelwerte")
_ = fig.suptitle("Waschbärenbild, komprimiert mit 3 Bits und einer K-Means-Strategie")
```

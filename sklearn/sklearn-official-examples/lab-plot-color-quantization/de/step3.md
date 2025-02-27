# K-Means-Modell anpassen

Wir werden das K-Means-Modell an einem kleinen Teilstichproben der Bilddaten anpassen und es verwenden, um Farb-Indizes für das gesamte Bild vorherzusagen.

```python
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from time import time

n_colors = 64

# Passt das K-Means-Modell an einem kleinen Teilstichproben der Daten an
print("Anpassen des Modells an einem kleinen Teilstichproben der Daten")
t0 = time()
image_array_sample = shuffle(image_array, random_state=0, n_samples=1000)
kmeans = KMeans(n_clusters=n_colors, n_init="auto", random_state=0).fit(
    image_array_sample
)
print(f"fertig in {time() - t0:0.3f}s.")

# Holt die Labels für alle Punkte
print("Vorhersagen von Farb-Indizes für das gesamte Bild (k-means)")
t0 = time()
labels = kmeans.predict(image_array)
print(f"fertig in {time() - t0:0.3f}s.")
```

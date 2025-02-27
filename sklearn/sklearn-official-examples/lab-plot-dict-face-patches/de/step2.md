# Lernen des Bildwörterbuchs

Wir verwenden MiniBatchKMeans, um das Bildwörterbuch zu lernen. Wir setzen die Anzahl der Cluster auf 81, legen einen Zufallszustand fest und aktivieren den detaillierten Modus. Anschließend erstellen wir einen Puffer, um die Ausschnitte zu speichern, und iterieren über jedes Bild im Datensatz. Wir extrahieren 50 Ausschnitte aus jedem Bild und formen die Daten um. Danach fügen wir die Daten dem Puffer hinzu und erhöhen den Index. Wenn der Index ein Vielfaches von 10 ist, verbinden wir den Puffer und führen partial_fit auf den Daten aus. Wenn der Index ein Vielfaches von 100 ist, geben wir eine Nachricht aus, die die Anzahl der bisher angepassten Ausschnitte angibt.

```python
import time
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.image import extract_patches_2d

print("Learning the dictionary... ")
rng = np.random.RandomState(0)
kmeans = MiniBatchKMeans(n_clusters=81, random_state=rng, verbose=True, n_init=3)
patch_size = (20, 20)

buffer = []
t0 = time.time()

# The online learning part: cycle over the whole dataset 6 times
index = 0
for _ in range(6):
    for img in faces.images:
        data = extract_patches_2d(img, patch_size, max_patches=50, random_state=rng)
        data = np.reshape(data, (len(data), -1))
        buffer.append(data)
        index += 1
        if index % 10 == 0:
            data = np.concatenate(buffer, axis=0)
            data -= np.mean(data, axis=0)
            data /= np.std(data, axis=0)
            kmeans.partial_fit(data)
            buffer = []
        if index % 100 == 0:
            print("Partial fit of %4i out of %i" % (index, 6 * len(faces.images)))

dt = time.time() - t0
print("done in %.2fs." % dt)
```

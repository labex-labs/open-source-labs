# Datensatz laden und erkunden

```python
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
n_samples, h, w = lfw_people.images.shape
X = lfw_people.data
n_features = X.shape[1]
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]
```

Wir laden den Datensatz mit der Funktion `fetch_lfw_people()` aus scikit-learn herunter. Anschließend erkunden wir den Datensatz, indem wir die Anzahl der Bilder, die Höhe und die Breite ermitteln. Wir erhalten auch die Eingabedaten `X`, das Ziel `y`, die Zielnamen `target_names` und die Anzahl der Klassen `n_classes`.
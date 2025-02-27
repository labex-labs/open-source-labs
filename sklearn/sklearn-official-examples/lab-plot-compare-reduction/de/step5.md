# Cachen von Transformatoren in einer Pipeline

Wir werden nun demonstrieren, wie der Zustand eines bestimmten Transformators gespeichert werden kann, da er wieder verwendet werden könnte. Das Verwenden einer Pipeline in `GridSearchCV` löst solche Situationen aus. Daher verwenden wir das Argument `memory`, um das Caching zu aktivieren.

```python
from joblib import Memory
from shutil import rmtree

# Erstelle einen temporären Ordner, um die Transformatoren der Pipeline zu speichern
location = "cachedir"
memory = Memory(location=location, verbose=10)
cached_pipe = Pipeline(
    [("reduce_dim", PCA()), ("classify", LinearSVC(dual=False, max_iter=10000))],
    memory=memory,
)

# Diesmal wird eine gecachte Pipeline im Grid-Search verwendet

# Lösche den temporären Cache vor dem Beenden
memory.clear(warn=False)
rmtree(location)
```

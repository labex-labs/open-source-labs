# Caching von Transformatoren

Das Anpassen von Transformatoren kann rechenintensiv sein. Um wiederholte Berechnungen zu vermeiden, können Sie die Caching von Transformatoren in einer Pipeline mithilfe des Parameters `memory` aktivieren. Dieser Parameter kann auf ein Verzeichnis festgelegt werden, in dem die Transformatoren zwischengespeichert werden, oder auf ein `joblib.Memory`-Objekt. Hier ist ein Beispiel:

```python
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from tempfile import mkdtemp
from shutil import rmtree

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
cachedir = mkdtemp()
pipe = Pipeline(estimators, memory=cachedir)

# Leeren Sie das Cachedir, wenn es nicht mehr benötigt wird
rmtree(cachedir)
```

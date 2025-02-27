# Caché de Transformadores

Ajustar transformadores puede ser computacionalmente costoso. Para evitar la computación repetida, puede habilitar el caché de transformadores en una tubería utilizando el parámetro `memory`. Este parámetro se puede establecer en un directorio donde se almacenarán en caché los transformadores, o en un objeto `joblib.Memory`. Aquí hay un ejemplo:

```python
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from tempfile import mkdtemp
from shutil import rmtree

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
cachedir = mkdtemp()
pipe = Pipeline(estimators, memory=cachedir)

# Borre el directorio de caché cuando ya no sea necesario
rmtree(cachedir)
```

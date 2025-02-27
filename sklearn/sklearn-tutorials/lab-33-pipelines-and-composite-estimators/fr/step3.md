# Mémorisation des transformateurs

La mise en forme des transformateurs peut être coûteuse en termes de calcul. Pour éviter les calculs répétés, vous pouvez activer la mémorisation des transformateurs dans un pipeline en utilisant le paramètre `memory`. Ce paramètre peut être défini sur un répertoire où les transformateurs seront mis en cache, ou sur un objet `joblib.Memory`. Voici un exemple :

```python
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from tempfile import mkdtemp
from shutil import rmtree

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
cachedir = mkdtemp()
pipe = Pipeline(estimators, memory=cachedir)

# Supprimez le répertoire de cache lorsque vous n'en avez plus besoin
rmtree(cachedir)
```

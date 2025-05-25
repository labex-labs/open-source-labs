# Memorização de Transformadores

Ajustar transformadores pode ser computacionalmente dispendioso. Para evitar cálculos repetidos, pode ativar a memorização de transformadores num pipeline usando o parâmetro `memory`. Este parâmetro pode ser definido para um diretório onde os transformadores serão armazenados em cache, ou para um objeto `joblib.Memory`. Aqui está um exemplo:

```python
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from tempfile import mkdtemp
from shutil import rmtree

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
cachedir = mkdtemp()
pipe = Pipeline(estimators, memory=cachedir)

# Limpar o diretório de cache quando não for mais necessário
rmtree(cachedir)
```

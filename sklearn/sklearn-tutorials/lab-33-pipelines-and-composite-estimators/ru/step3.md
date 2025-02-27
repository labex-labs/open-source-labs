# Кэширование трансформеров

Подгонка трансформеров может быть вычислительно затратной. Чтобы избежать повторных вычислений, вы можете включить кэширование трансформеров в конвейере с использованием параметра `memory`. Этот параметр можно установить в директорию, где трансформеры будут кэшированы, или в объект `joblib.Memory`. Вот пример:

```python
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from tempfile import mkdtemp
from shutil import rmtree

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
cachedir = mkdtemp()
pipe = Pipeline(estimators, memory=cachedir)

# Clear the cache directory when no longer needed
rmtree(cachedir)
```

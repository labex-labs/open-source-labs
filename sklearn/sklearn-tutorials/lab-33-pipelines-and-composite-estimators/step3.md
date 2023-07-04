# Caching Transformers

Fitting transformers can be computationally expensive. To avoid repeated computation, you can enable caching transformers in a pipeline using the `memory` parameter. This parameter can be set to a directory where the transformers will be cached, or to a `joblib.Memory` object. Here is an example:

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

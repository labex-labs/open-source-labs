# 缓存转换器

拟合转换器的计算成本可能很高。为避免重复计算，你可以使用 `memory` 参数在管道中启用缓存转换器。此参数可以设置为一个目录，转换器将被缓存到该目录中，或者设置为一个 `joblib.Memory` 对象。以下是一个示例：

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

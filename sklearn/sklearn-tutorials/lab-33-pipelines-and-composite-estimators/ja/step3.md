# トランスフォーマーのキャッシング

トランスフォーマーの適合は計算コストがかかる場合があります。繰り返しの計算を回避するために、`memory` パラメータを使用してパイプライン内でトランスフォーマーのキャッシングを有効にできます。このパラメータは、トランスフォーマーがキャッシュされるディレクトリ、または `joblib.Memory` オブジェクトに設定できます。以下は例です：

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

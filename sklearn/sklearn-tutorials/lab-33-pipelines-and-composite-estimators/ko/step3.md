# 변환기 캐싱

변환기를 맞추는 작업은 계산적으로 비용이 많이 들 수 있습니다. 반복적인 계산을 피하기 위해 파이프라인에서 `memory` 매개변수를 사용하여 변환기를 캐싱할 수 있습니다. 이 매개변수는 변환기가 캐싱될 디렉토리 또는 `joblib.Memory` 객체로 설정할 수 있습니다. 예제는 다음과 같습니다.

```python
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from tempfile import mkdtemp
from shutil import rmtree

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
cachedir = mkdtemp()
pipe = Pipeline(estimators, memory=cachedir)

# 더 이상 필요하지 않을 때 캐시 디렉토리를 지웁니다.
rmtree(cachedir)
```

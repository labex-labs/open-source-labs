# 파이프라인 내 변환기 캐싱

특정 변환기의 상태를 저장하여 재사용할 수 있도록 하는 방법을 보여줍니다. `GridSearchCV`에서 파이프라인을 사용하면 이러한 상황이 발생합니다. 따라서 캐싱을 활성화하기 위해 `memory` 인수를 사용합니다.

```python
from joblib import Memory
from shutil import rmtree

# 파이프라인의 변환기 상태를 저장할 임시 폴더 생성
location = "cachedir"
memory = Memory(location=location, verbose=10)
cached_pipe = Pipeline(
    [("reduce_dim", PCA()), ("classify", LinearSVC(dual=False, max_iter=10000))],
    memory=memory,
)

# 이번에는 그리드 검색 내에서 캐싱된 파이프라인이 사용됩니다.

# 종료 전 임시 캐시 삭제
memory.clear(warn=False)
rmtree(location)
```

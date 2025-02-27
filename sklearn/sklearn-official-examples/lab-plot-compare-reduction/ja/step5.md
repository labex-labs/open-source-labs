# パイプライン内でトランスフォーマーをキャッシュする

特定のトランスフォーマーの状態を保存する方法を示します。再度使用できる場合があるためです。`GridSearchCV` でパイプラインを使用すると、このような状況が発生します。したがって、キャッシュを有効にするために `memory` 引数を使用します。

```python
from joblib import Memory
from shutil import rmtree

# Create a temporary folder to store the transformers of the pipeline
location = "cachedir"
memory = Memory(location=location, verbose=10)
cached_pipe = Pipeline(
    [("reduce_dim", PCA()), ("classify", LinearSVC(dual=False, max_iter=10000))],
    memory=memory,
)

# This time, a cached pipeline will be used within the grid search

# Delete the temporary cache before exiting
memory.clear(warn=False)
rmtree(location)
```

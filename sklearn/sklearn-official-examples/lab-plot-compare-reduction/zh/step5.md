# 在管道中缓存转换器

现在我们将演示如何存储特定转换器的状态，因为它可能会被再次使用。在`GridSearchCV`中使用管道会引发这种情况。因此，我们使用参数`memory`来启用缓存。

```python
from joblib import Memory
from shutil import rmtree

# 创建一个临时文件夹来存储管道的转换器
location = "cachedir"
memory = Memory(location=location, verbose=10)
cached_pipe = Pipeline(
    [("reduce_dim", PCA()), ("classify", LinearSVC(dual=False, max_iter=10000))],
    memory=memory,
)

# 这次，将在网格搜索中使用缓存的管道

# 在退出前删除临时缓存
memory.clear(warn=False)
rmtree(location)
```

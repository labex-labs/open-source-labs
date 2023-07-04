# Caching transformers within a Pipeline

We will now demonstrate how to store the state of a specific transformer, since it could be used again. Using a pipeline in `GridSearchCV` triggers such situations. Therefore, we use the argument `memory` to enable caching.

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

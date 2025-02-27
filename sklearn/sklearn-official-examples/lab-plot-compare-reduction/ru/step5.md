# Кэширование трансформеров внутри конвейера

Теперь мы покажем, как сохранять состояние определенного трансформера, так как он может быть использован снова. Использование конвейера в `GridSearchCV` приводит к подобным ситуациям. Поэтому мы используем аргумент `memory` для включения кэширования.

```python
from joblib import Memory
from shutil import rmtree

# Создаем временную папку для хранения трансформеров конвейера
location = "cachedir"
memory = Memory(location=location, verbose=10)
cached_pipe = Pipeline(
    [("reduce_dim", PCA()), ("classify", LinearSVC(dual=False, max_iter=10000))],
    memory=memory,
)

# На этот раз в сеточном поиске будет использоваться кэшированный конвейер

# Удаляем временный кэш перед выходом
memory.clear(warn=False)
rmtree(location)
```

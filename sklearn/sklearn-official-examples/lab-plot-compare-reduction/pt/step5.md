# Armazenamento em cache de transformadores dentro de um Pipeline

Agora demonstraremos como armazenar o estado de um transformador específico, já que ele pode ser reutilizado. O uso de um pipeline em `GridSearchCV` aciona essas situações. Portanto, usamos o argumento `memory` para habilitar o armazenamento em cache.

```python
from joblib import Memory
from shutil import rmtree

# Crie uma pasta temporária para armazenar os transformadores do pipeline
location = "cachedir"
memory = Memory(location=location, verbose=10)
cached_pipe = Pipeline(
    [("reduce_dim", PCA()), ("classify", LinearSVC(dual=False, max_iter=10000))],
    memory=memory,
)

# Desta vez, um pipeline em cache será usado na busca em grade

# Exclua o cache temporário antes de sair
memory.clear(warn=False)
rmtree(location)
```

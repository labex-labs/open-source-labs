# Mémorisation des transformateurs dans un Pipeline

Nous allons maintenant démontrer comment stocker l'état d'un transformateur spécifique, car il pourrait être utilisé à nouveau. L'utilisation d'un pipeline dans `GridSearchCV` déclenche de telles situations. Par conséquent, nous utilisons l'argument `memory` pour activer la mémorisation.

```python
from joblib import Memory
from shutil import rmtree

# Créez un dossier temporaire pour stocker les transformateurs du pipeline
location = "cachedir"
memory = Memory(location=location, verbose=10)
cached_pipe = Pipeline(
    [("reduce_dim", PCA()), ("classify", LinearSVC(dual=False, max_iter=10000))],
    memory=memory,
)

# Cette fois, un pipeline mis en cache sera utilisé dans la recherche en grille

# Supprimez le cache temporaire avant de quitter
memory.clear(warn=False)
rmtree(location)
```

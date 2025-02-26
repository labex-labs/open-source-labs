# Commentaires sur l'importation

Les variations de l'importation _ne changent pas_ la manière dont les modules fonctionnent.

```python
import math
# vs
import math as m
# vs
from math import cos, sin
...
```

Plus précisément, `import` exécute toujours _tout le fichier_ et les modules restent des environnements isolés.

L'instruction `import module as` ne fait que changer le nom localement. L'instruction `from math import cos, sin` charge toujours le module mathématique en arrière-plan. Elle ne fait que copier les noms `cos` et `sin` du module dans l'espace local une fois qu'elle est terminée.

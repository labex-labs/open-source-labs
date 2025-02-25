# Activation du Copy-On-Write

Tout d'abord, activons le CoW dans pandas. Cela peut être fait à l'aide de l'option de configuration `copy_on_write` dans pandas. Voici deux façons de l'activer globalement.

```python
# Importation des bibliothèques pandas et numpy
import pandas as pd

# Activer le CoW en utilisant set_option
pd.set_option("mode.copy_on_write", True)

# Ou en utilisant une affectation directe
pd.options.mode.copy_on_write = True
```

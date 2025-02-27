# Importez les bibliothèques requises et définissez les constantes

Tout d'abord, nous devons importer les bibliothèques requises et définir les couleurs et la constante de graine aléatoire pour générer l'ensemble de données à étiquetage multiple.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_multilabel_classification as make_ml_clf

COLORS = np.array(
    [
        "!",
        "#FF3333",  # rouge
        "#0198E1",  # bleu
        "#BF5FFF",  # violet
        "#FCD116",  # jaune
        "#FF7216",  # orange
        "#4DBD33",  # vert
        "#87421F",  # brun
    ]
)

# Utilisez la même graine aléatoire pour plusieurs appels à make_multilabel_classification pour
# vous assurer d'avoir les mêmes distributions
RANDOM_SEED = np.random.randint(2**10)
```

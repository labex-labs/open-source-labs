# Convertissez les chaînes de caractères en types numériques

Pour corriger le comportement des étiquettes d'échelle, nous devons convertir les chaînes de caractères en types numériques. Voici un exemple :

```python
import matplotlib.pyplot as plt
import numpy as np

# créez des données d'exemple
x = ['1', '5', '2', '3']
y = [1, 4, 2, 3]

# convertissez les chaînes de caractères en flottants
x = np.asarray(x, dtype='float')

# tracez les données avec des étiquettes d'échelle numériques
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.set_xlabel('Floats')
plt.show()
```

Dans cet exemple, nous convertissons les valeurs de chaîne de caractères en flottants à l'aide de `np.asarray()`. Lorsque nous traçons à nouveau les données, les étiquettes d'échelle sont comme attendu.

# Gérer les étiquettes de date et d'heure

Lorsque l'on travaille avec des valeurs de date et d'heure sur l'axe x, il est important de convertir les chaînes de caractères en objets de date et d'heure pour obtenir les localisateurs et les formatteurs de date appropriés. Voici un exemple :

```python
import matplotlib.pyplot as plt
import numpy as np

# créez des données d'exemple avec des chaînes de caractères de date et d'heure
x = ['2021-10-01', '2021-11-02', '2021-12-03', '2021-09-01']
y = [0, 2, 3, 1]

# convertissez les chaînes de caractères en datetime64
x = np.asarray(x, dtype='datetime64[s]')

# tracez les données avec des étiquettes d'échelle de date et d'heure
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.tick_params(axis='x', labelrotation=90)
plt.show()
```

Dans cet exemple, nous convertissons les valeurs de chaîne de caractères en datetime64 à l'aide de `np.asarray()`. Lorsque nous traçons à nouveau les données, les étiquettes d'échelle sont comme attendu.

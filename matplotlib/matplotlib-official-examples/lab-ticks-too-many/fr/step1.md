# Vérifiez le type de données

La première étape consiste à vérifier le type de données des valeurs de l'axe x. Si c'est une liste de chaînes de caractères, il est probable que le comportement des étiquettes d'échelle soit inattendu. Pour corriger ceci, nous devons convertir les chaînes de caractères en types numériques. Voici un exemple :

```python
import matplotlib.pyplot as plt
import numpy as np

# créez des données d'exemple
x = ['1', '5', '2', '3']
y = [1, 4, 2, 3]

# tracez les données avec des étiquettes d'échelle de type chaîne de caractères
fig, ax = plt.subplots()
ax.plot(x, y, 'd')
ax.set_xlabel('Categories')
plt.show()
```

Dans cet exemple, nous avons une liste de chaînes de caractères sur l'axe x. Lorsque nous traçons les données, les étiquettes d'échelle sont désordonnées et mal placées.

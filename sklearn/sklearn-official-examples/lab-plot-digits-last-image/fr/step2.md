# Visualisation de l'ensemble de données

Pour mieux comprendre l'ensemble de données, nous pouvons visualiser une image d'échantillon à l'aide de matplotlib. Le code suivant affiche le dernier chiffre dans l'ensemble de données :

```python
import matplotlib.pyplot as plt

# Affiche le dernier chiffre
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
```

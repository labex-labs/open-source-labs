# Choisir une police sans-serif spécifique

Si nous souhaitons utiliser une police sans-serif spécifique, nous pouvons configurer le paramètre `font.sans-serif` avec une liste de noms de polices. Matplotlib tentera d'utiliser la première police de la liste disponible sur le système de l'utilisateur. Pour ce faire, nous pouvons utiliser le code suivant :

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Nimbus Sans"]
```

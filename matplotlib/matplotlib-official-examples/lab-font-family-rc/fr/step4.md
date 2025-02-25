# Choisir une police monospace spécifique

Si nous souhaitons utiliser une police monospace spécifique, nous pouvons configurer le paramètre `font.monospace` avec une liste de noms de polices. Matplotlib tentera d'utiliser la première police de la liste disponible sur le système de l'utilisateur. Pour ce faire, nous pouvons utiliser le code suivant :

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
plt.rcParams["font.monospace"] = ["FreeMono"]
```

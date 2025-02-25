# Choisir la police monospace par défaut

La police monospace par défaut dans Matplotlib est déterminée par le système d'exploitation. Nous pouvons choisir d'utiliser la police monospace par défaut en configurant le paramètre `font.family` avec la valeur `'monospace'`. Pour ce faire, nous pouvons utiliser le code suivant :

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
```

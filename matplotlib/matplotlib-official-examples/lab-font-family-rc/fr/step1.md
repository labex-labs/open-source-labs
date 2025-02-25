# Choisir la police sans-serif par défaut

La famille de police par défaut dans Matplotlib est sans-serif. Nous pouvons choisir d'utiliser la famille de police par défaut en configurant le paramètre `font.family` avec la valeur `'sans-serif'`. Pour ce faire, nous pouvons utiliser le code suivant :

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
```

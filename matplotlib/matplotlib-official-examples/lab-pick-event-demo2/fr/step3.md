# Tracer les données

Maintenant, nous allons tracer mu en fonction de sigma à l'aide du module `pyplot` de Matplotlib. Nous allons créer un graphique en points à dispersion à l'aide des valeurs calculées pour mu et sigma. Nous ajouterons également une interactivité au graphique en définissant le paramètre `picker` sur True.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title('click on point to plot time series')
line, = ax.plot(xs, ys, 'o', picker=True, pickradius=5)
```

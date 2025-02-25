# Configuration des étiquettes d'échelle

Par défaut, les étiquettes d'échelle aux valeurs négatives sont affichées avec un moins Unicode plutôt qu'un tiret ASCII. Cependant, nous pouvons modifier ce comportement en configurant `axes.unicode_minus` sur `False`.

```python
plt.rcParams['axes.unicode_minus'] = False
```

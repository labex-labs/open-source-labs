# Diagramme en points avec mode d'autolimitation round_numbers

Dans cette étape, nous allons basculer `axes.autolimit_mode` sur 'round_numbers' et créer un diagramme en points pour maintenir les graduations à des nombres arrondis et également avoir des graduations sur les bords.

```python
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

fig, ax = plt.subplots()
ax.scatter(x, y, c=x+y)
plt.show()
```

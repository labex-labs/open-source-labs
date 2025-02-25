# Créer des graphiques

Dans cette étape, nous allons créer deux graphiques - l'un utilisant des unités personnalisées et l'autre utilisant les unités par défaut.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("Unités personnalisées")
fig.subplots_adjust(bottom=0.2)

# tracer en spécifiant les unités
ax2.plot(x, y, 'o', xunits=2.0)
ax2.set_title("xunits = 2.0")
plt.setp(ax2.get_xticklabels(), rotation=30, ha='right')

# tracer sans spécifier les unités ; utilisera la branche None pour axisinfo
ax1.plot(x, y)  # utilise les unités par défaut
ax1.set_title('Unités par défaut')
plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

plt.show()
```

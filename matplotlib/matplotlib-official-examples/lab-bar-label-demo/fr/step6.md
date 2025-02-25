# Étiquetage des barres en utilisant une fonction appelable

Enfin, nous allons montrer comment utiliser une fonction appelable pour formater les étiquettes des barres. Nous utiliserons certaines données sur les vitesses de course de différents animaux.

```python
animal_names = ['Lion', 'Gazelle', 'Cheetah']
mph_speed = [50, 60, 75]

fig, ax = plt.subplots()
bar_container = ax.bar(animal_names, mph_speed)
ax.set(ylabel='vitesse en mph', title='Vitesses de course', ylim=(0, 80))
ax.bar_label(bar_container, fmt=lambda x: f'{x * 1.61:.1f} km/h')
```

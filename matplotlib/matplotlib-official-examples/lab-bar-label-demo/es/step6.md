# Etiquetado de barras usando una función llamada

Finalmente, mostraremos cómo usar una función llamada para formatear las etiquetas de barras. Usaremos algunos datos sobre las velocidades de diferentes animales al correr.

```python
animal_names = ['Lion', 'Gazelle', 'Cheetah']
mph_speed = [50, 60, 75]

fig, ax = plt.subplots()
bar_container = ax.bar(animal_names, mph_speed)
ax.set(ylabel='speed in MPH', title='Running speeds', ylim=(0, 80))
ax.bar_label(bar_container, fmt=lambda x: f'{x * 1.61:.1f} km/h')
```

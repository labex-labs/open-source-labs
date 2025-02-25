# Balkenbeschriftung mit einer aufrufbaren Funktion

Schließlich zeigen wir, wie eine aufrufbare Funktion verwendet werden kann, um Balkenbeschriftungen zu formatieren. Wir verwenden einige Daten über die Laufgeschwindigkeiten verschiedener Tiere.

```python
animal_names = ['Lion', 'Gazelle', 'Cheetah']
mph_speed = [50, 60, 75]

fig, ax = plt.subplots()
bar_container = ax.bar(animal_names, mph_speed)
ax.set(ylabel='speed in MPH', title='Running speeds', ylim=(0, 80))
ax.bar_label(bar_container, fmt=lambda x: f'{x * 1.61:.1f} km/h')
```

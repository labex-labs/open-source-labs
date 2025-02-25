# Ajouter un titre, une étiquette pour l'axe des x et une étiquette pour l'axe des y

Nous pouvons ajouter un titre, une étiquette pour l'axe des x et une étiquette pour l'axe des y au graphique à l'aide des méthodes `title()`, `xlabel()` et `ylabel()` de la bibliothèque `pyplot`. Nous allons ajouter "Tension en fonction du temps" comme titre, "Temps [s]" comme étiquette pour l'axe des x et "Tension [mV]" comme étiquette pour l'axe des y.

```python
plt.title(r'Voltage vs Time', fontsize=20)
plt.xlabel('Time [s]')
plt.ylabel('Voltage [mV]')
```

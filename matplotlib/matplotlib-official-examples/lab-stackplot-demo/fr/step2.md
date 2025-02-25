# Création d'un graphique empilé

La deuxième étape consiste à créer un graphique empilé à l'aide de la fonction `stackplot()`. Nous utiliserons les données des Perspectives démographiques mondiales de l'ONU (Révision 2019) pour créer un graphique empilé de la population mondiale par continent de 1950 à 2018.

```python
# données des Perspectives démographiques mondiales de l'ONU (Révision 2019)
# https://population.un.org/wpp/, licence : CC BY 3.0 IGO
year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2018]
population_by_continent = {
    'afrique': [228, 284, 365, 477, 631, 814, 1044, 1275],
    'amériques': [340, 425, 519, 619, 727, 840, 943, 1006],
    'asie': [1394, 1686, 2120, 2625, 3202, 3714, 4169, 4560],
    'europe': [220, 253, 276, 295, 310, 303, 294, 293],
    'océanie': [12, 15, 19, 22, 26, 31, 36, 39],
}

fig, ax = plt.subplots()
ax.stackplot(year, population_by_continent.values(),
             labels=population_by_continent.keys(), alpha=0.8)
ax.legend(loc='upper left', reverse=True)
ax.set_title('Population mondiale')
ax.set_xlabel('Année')
ax.set_ylabel('Nombre de personnes (en millions)')

plt.show()
```

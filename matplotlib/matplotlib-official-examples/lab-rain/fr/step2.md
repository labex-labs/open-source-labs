# Créer des données de pluie

Ensuite, nous allons créer les données de pluie. Nous allons créer 50 gouttes de pluie en positions aléatoires, avec des taux de croissance aléatoires et des couleurs aléatoires.

```python
n_drops = 50
rain_drops = np.zeros(n_drops, dtype=[('position', float, (2,)),
                                      ('size',     float),
                                      ('growth',   float),
                                      ('color',    float, (4,))])

rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)
```

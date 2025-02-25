# Regen-Daten erstellen

Als nächstes werden wir die Regen-Daten erstellen. Wir werden 50 Regentropfen an zufälligen Positionen mit zufälligen Wachstumsraten und zufälligen Farben erzeugen.

```python
n_drops = 50
rain_drops = np.zeros(n_drops, dtype=[('position', float, (2,)),
                                      ('size',     float),
                                      ('growth',   float),
                                      ('color',    float, (4,))])

rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)
```

# Definieren der Zufallswalk-Funktion

Wir definieren eine Funktion, die einen Zufallswalk mit einer angegebenen Anzahl von Schritten und einer maximalen Schrittgröße generiert. Die Funktion nimmt zwei Eingaben entgegen: `num_steps` ist die Gesamtzahl der Schritte im Zufallswalk und `max_step` ist die maximale Größe jedes Schritts. Wir verwenden `numpy.random`, um Zufallszahlen für die Schritte zu generieren, und `numpy.cumsum`, um die kumulative Summe der Schritte zu berechnen, um die Endposition zu erhalten.

```python
def random_walk(num_steps, max_step=0.05):
    """Return a 3D random walk as (num_steps, 3) array."""
    start_pos = np.random.random(3)
    steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
    walk = start_pos + np.cumsum(steps, axis=0)
    return walk
```

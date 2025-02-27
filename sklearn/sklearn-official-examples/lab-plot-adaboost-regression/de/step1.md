# Vorbereitung der Daten

Wir beginnen mit der Vorbereitung von Dummy-Daten mit einer sinusförmigen Beziehung und etwas Gauß'scher Rauschen. Wir verwenden die `linspace()`-Funktion von Numpy, um ein eindimensionales Array mit 100 gleichmäßig verteilten Werten zwischen 0 und 6 zu erstellen. Anschließend verwenden wir das Attribut `np.newaxis`, um das eindimensionale Array in ein zweidimensionales Array der Form `(100,1)` umzuwandeln. Wir wenden die `sin()`-Funktion auf dieses Array an und addieren eine zweite Sinuswelle, die durch Multiplikation des Arrays mit 6 erhalten wird. Anschließend fügen wir mit der `normal()`-Funktion von Numpy etwas Gauß'sches Rauschen mit einem Mittelwert von 0 und einer Standardabweichung von 0,1 hinzu.

```python
import numpy as np

rng = np.random.RandomState(1)
X = np.linspace(0, 6, 100)[:, np.newaxis]
y = np.sin(X).ravel() + np.sin(6 * X).ravel() + rng.normal(0, 0.1, X.shape[0])
```

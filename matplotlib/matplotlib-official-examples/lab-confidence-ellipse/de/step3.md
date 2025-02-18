# Definition der Funktion `get_correlated_dataset`

Wir benötigen auch eine Funktion, um einen zweidimensionalen Datensatz mit einem angegebenen Mittelwert, Dimensionen und Korrelation zu generieren.

```python
def get_correlated_dataset(n, dependency, mu, scale):
    """
    Erstellt einen zufälligen zweidimensionalen Datensatz mit dem angegebenen
    zweidimensionalen Mittelwert (mu) und Dimensionen (scale).
    Die Korrelation kann über den Parameter 'dependency', eine 2x2-Matrix, gesteuert werden.
    """
    latent = np.random.randn(n, 2)
    dependent = latent.dot(dependency)
    scaled = dependent * scale
    scaled_with_offset = scaled + mu
    # Gibt x und y des neuen, korrelierten Datensatzes zurück
    return scaled_with_offset[:, 0], scaled_with_offset[:, 1]
```

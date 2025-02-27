# Definiere Ricker-Wellenlet-Funktionen

Wir werden Funktionen definieren, um einen Ricker-Wellenlet und ein Wörterbuch von Ricker-Wellenletten zu generieren.

```python
def ricker_function(resolution, center, width):
    """Diskreter sub-samplierter Ricker (Mexikanischer Hut) -Wellenlet"""
    x = np.linspace(0, resolution - 1, resolution)
    x = (
        (2 / (np.sqrt(3 * width) * np.pi**0.25))
        * (1 - (x - center) ** 2 / width**2)
        * np.exp(-((x - center) ** 2) / (2 * width**2))
    )
    return x


def ricker_matrix(width, resolution, n_components):
    """Wörterbuch von Ricker (Mexikanischer Hut) -Wellenletten"""
    centers = np.linspace(0, resolution - 1, n_components)
    D = np.empty((n_components, resolution))
    for i, center in enumerate(centers):
        D[i] = ricker_function(resolution, center, width)
    D /= np.sqrt(np.sum(D**2, axis=1))[:, np.newaxis]
    return D
```

# Utilisez l'échelle personnalisée

Maintenant, nous pouvons utiliser l'échelle personnalisée dans nos tracés. Voici un exemple d'utilisation de l'échelle personnalisée pour les données de latitude dans une projection Mercator.

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    t = np.arange(-180.0, 180.0, 0.1)
    s = np.radians(t)/2.

    plt.plot(t, s, '-', lw=2)
    plt.yscale('mercator')

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Projection Mercator')
    plt.grid(True)

    plt.show()
```

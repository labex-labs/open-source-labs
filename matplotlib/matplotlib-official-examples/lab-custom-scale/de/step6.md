# Verwenden der benutzerdefinierten Skala

Jetzt können wir die benutzerdefinierte Skala in unseren Plots verwenden. Hier ist ein Beispiel für die Verwendung der benutzerdefinierten Skala für Breitengraddaten bei einer Mercator-Projektion.

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    t = np.arange(-180.0, 180.0, 0.1)
    s = np.radians(t)/2.

    plt.plot(t, s, '-', lw=2)
    plt.yscale('mercator')

    plt.xlabel('Längengrad')
    plt.ylabel('Breitengrad')
    plt.title('Mercator-Projektion')
    plt.grid(True)

    plt.show()
```

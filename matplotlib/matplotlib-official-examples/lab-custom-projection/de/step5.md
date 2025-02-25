# Beispiel erstellen

Schließlich werden wir ein Beispiel mit der benutzerdefinierten Projektion erstellen.

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    # Jetzt erstellen wir ein einfaches Beispiel mit der benutzerdefinierten Projektion.
    fig, ax = plt.subplots(subplot_kw={'projection': 'custom_hammer'})
    ax.plot([-1, 1, 1], [-1, -1, 1], "o-")
    ax.grid()

    plt.show()
```

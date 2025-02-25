# Créer un exemple

Enfin, nous allons créer un exemple utilisant la projection personnalisée.

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    # Maintenant, créons un exemple simple utilisant la projection personnalisée.
    fig, ax = plt.subplots(subplot_kw={'projection': 'custom_hammer'})
    ax.plot([-1, 1, 1], [-1, -1, 1], "o-")
    ax.grid()

    plt.show()
```

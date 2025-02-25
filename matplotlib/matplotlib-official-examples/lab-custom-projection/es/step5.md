# Crear un ejemplo

Finalmente, crearemos un ejemplo utilizando la proyección personalizada.

```python
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    # Ahora hagamos un ejemplo simple utilizando la proyección personalizada.
    fig, ax = plt.subplots(subplot_kw={'projection': 'custom_hammer'})
    ax.plot([-1, 1, 1], [-1, -1, 1], "o-")
    ax.grid()

    plt.show()
```

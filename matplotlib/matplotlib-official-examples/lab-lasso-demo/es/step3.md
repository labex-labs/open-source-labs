# Crear la trama

Ahora, use la clase `LassoManager` para crear una trama interactiva. La función `np.random.rand` genera puntos de datos aleatorios que se graficarán.

```python
if __name__ == '__main__':
    np.random.seed(19680801)
    ax = plt.figure().add_subplot(
        xlim=(0, 1), ylim=(0, 1), title='Lasso points using left mouse button')
    manager = LassoManager(ax, np.random.rand(100, 2))
    plt.show()
```

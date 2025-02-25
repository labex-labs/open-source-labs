# Erstellen des Plots

Jetzt verwenden wir die `LassoManager`-Klasse, um einen interaktiven Plot zu erstellen. Die `np.random.rand`-Funktion generiert zufällige Datenpunkte, die geplottet werden.

```python
if __name__ == '__main__':
    np.random.seed(19680801)
    ax = plt.figure().add_subplot(
        xlim=(0, 1), ylim=(0, 1), title='Lasso points using left mouse button')
    manager = LassoManager(ax, np.random.rand(100, 2))
    plt.show()
```

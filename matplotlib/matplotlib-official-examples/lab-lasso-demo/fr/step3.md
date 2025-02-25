# Créer le graphique

Maintenant, utilisez la classe `LassoManager` pour créer un graphique interactif. La fonction `np.random.rand` génère des points de données aléatoires qui seront tracés.

```python
if __name__ == '__main__':
    np.random.seed(19680801)
    ax = plt.figure().add_subplot(
        xlim=(0, 1), ylim=(0, 1), title='Lasso points using left mouse button')
    manager = LassoManager(ax, np.random.rand(100, 2))
    plt.show()
```

# Génération d'un diagramme de Hinton

Maintenant, nous allons générer une matrice de poids aléatoire à l'aide de numpy puis utiliser la fonction `hinton` pour générer le diagramme de Hinton.

```python
if __name__ == '__main__':
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    hinton(np.random.rand(20, 20) - 0.5)
    plt.show()
```

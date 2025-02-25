# Generando un diagrama de Hinton

Ahora, generaremos una matriz de pesos aleatoria usando numpy y luego usaremos la función `hinton` para generar el diagrama de Hinton.

```python
if __name__ == '__main__':
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    hinton(np.random.rand(20, 20) - 0.5)
    plt.show()
```

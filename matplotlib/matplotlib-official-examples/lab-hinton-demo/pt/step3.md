# Gerando um Diagrama de Hinton

Agora, geraremos uma matriz de pesos aleatórios usando numpy e, em seguida, usaremos a função `hinton` para gerar o diagrama de Hinton.

```python
if __name__ == '__main__':
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    hinton(np.random.rand(20, 20) - 0.5)
    plt.show()
```

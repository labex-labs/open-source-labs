# Criar o Gráfico

Agora, use a classe `LassoManager` para criar um gráfico interativo. A função `np.random.rand` gera pontos de dados aleatórios que serão plotados.

```python
if __name__ == '__main__':
    np.random.seed(19680801)
    ax = plt.figure().add_subplot(
        xlim=(0, 1), ylim=(0, 1), title='Lasso points using left mouse button')
    manager = LassoManager(ax, np.random.rand(100, 2))
    plt.show()
```

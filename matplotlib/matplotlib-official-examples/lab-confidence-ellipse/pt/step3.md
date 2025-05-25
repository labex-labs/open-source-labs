# Definir a Função `get_correlated_dataset`

Também precisamos de uma função para gerar um conjunto de dados bidimensional com média, dimensões e correlação especificadas.

```python
def get_correlated_dataset(n, dependency, mu, scale):
    """
    Cria um conjunto de dados bidimensional aleatório com a
    média bidimensional especificada (mu) e dimensões (scale).
    A correlação pode ser controlada pelo parâmetro 'dependency',
    uma matriz 2x2.
    """
    latent = np.random.randn(n, 2)
    dependent = latent.dot(dependency)
    scaled = dependent * scale
    scaled_with_offset = scaled + mu
    # return x and y of the new, correlated dataset
    return scaled_with_offset[:, 0], scaled_with_offset[:, 1]
```

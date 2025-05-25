# Carregar ou gerar conjuntos de dados pequenos

Agora, precisamos carregar ou gerar os pequenos conjuntos de dados que usaremos neste exemplo. Usaremos o conjunto de dados iris, o conjunto de dados digits e dois conjuntos de dados gerados usando as funções `make_circles` e `make_moons`.

```python
iris = datasets.load_iris()
X_digits, y_digits = datasets.load_digits(return_X_y=True)
data_sets = [
    (iris.data, iris.target),
    (X_digits, y_digits),
    datasets.make_circles(noise=0.2, factor=0.5, random_state=1),
    datasets.make_moons(noise=0.3, random_state=0),
]
```

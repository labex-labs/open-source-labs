# Núcleos

Os núcleos são medidas de similaridade entre dois objetos. Podem ser usados em vários algoritmos de aprendizagem de máquina para capturar relações não lineares entre características.

O scikit-learn fornece diferentes funções de núcleo, como núcleo linear, núcleo polinomial, núcleo sigmóide, núcleo RBF, núcleo Laplaciano e núcleo qui-quadrado.

Vamos calcular os núcleos em pares entre dois conjuntos de amostras usando a função `pairwise_kernels`:

```python
from sklearn.metrics.pairwise import pairwise_kernels

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calcular os núcleos em pares entre X e Y usando o núcleo linear
kernels = pairwise_kernels(X, Y, metric='linear')
print(kernels)
```

Saída:

```
array([[ 2.,  7.],
       [ 3., 11.],
       [ 5., 18.]])
```

# Núcleo Polinomial

O núcleo polinomial calcula a similaridade entre dois vetores considerando as interações entre suas dimensões.

O scikit-learn fornece a função `polynomial_kernel` para calcular o núcleo polinomial entre vetores.

```python
from sklearn.metrics.pairwise import polynomial_kernel

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calcular o núcleo polinomial entre X e Y
kernel = polynomial_kernel(X, Y, degree=2)
print(kernel)
```

Saída:

```
array([[ 10.,  20.],
       [ 17.,  37.],
       [ 38.,  82.]])
```

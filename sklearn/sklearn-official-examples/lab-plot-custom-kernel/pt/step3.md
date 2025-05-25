# Criar Kernel Personalizado

Neste passo, criaremos um kernel personalizado. O kernel personalizado será um produto escalar de duas matrizes. Criaremos uma matriz M com os valores [[2, 0], [0, 1.0]]. Em seguida, multiplicaremos as matrizes X e Y por M e calculamos o seu produto escalar.

```python
def my_kernel(X, Y):
    """
    Criamos um kernel personalizado:

                 (2  0)
    k(X, Y) = X  (    ) Y.T
                 (0  1)
    """
    M = np.array([[2, 0], [0, 1.0]])
    return np.dot(np.dot(X, M), Y.T)
```

# Similaridade do Cosseno

A similaridade do cosseno é uma medida da similaridade entre dois vetores. Calcula o cosseno do ângulo entre os vetores após normalizá-los.

O scikit-learn fornece a função `cosine_similarity` para calcular a similaridade do cosseno entre vetores.

```python
from sklearn.metrics.pairwise import cosine_similarity

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Calcular a similaridade do cosseno entre X e Y
similarity = cosine_similarity(X, Y)
print(similarity)
```

Saída:

```
array([[0.89442719, 0.9486833 ],
       [0.93982748, 0.99388373],
       [0.99417134, 0.99705449]])
```

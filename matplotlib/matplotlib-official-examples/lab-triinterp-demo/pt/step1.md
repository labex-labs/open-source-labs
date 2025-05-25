# Criar Triangulação

O primeiro passo é criar uma triangulação usando os dados x, y e triangles fornecidos. Em seguida, plotaremos a triangulação.

```python
# Create triangulation.
x = np.asarray([0, 1, 2, 3, 0.5, 1.5, 2.5, 1, 2, 1.5])
y = np.asarray([0, 0, 0, 0, 1.0, 1.0, 1.0, 2, 2, 3.0])
triangles = [[0, 1, 4], [1, 2, 5], [2, 3, 6], [1, 5, 4], [2, 6, 5], [4, 5, 7],
             [5, 6, 8], [5, 8, 7], [7, 8, 9]]
triang = mtri.Triangulation(x, y, triangles)

# Plot the triangulation.
plt.triplot(triang, 'ko-')
plt.title('Triangular grid')
plt.show()
```

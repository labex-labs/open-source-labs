# Comparar Resultados

Compara los resultados de los diferentes algoritmos de aprendizaje de variedades. Visualiza los datos transformados para ver cómo los algoritmos han preservado la estructura subyacente de los datos.

```python
import matplotlib.pyplot as plt

# Crea un diagrama de dispersión de los datos transformados
plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y)
plt.title('Aprendizaje de Variedades')
plt.xlabel('Componente 1')
plt.ylabel('Componente 2')
plt.show()
```

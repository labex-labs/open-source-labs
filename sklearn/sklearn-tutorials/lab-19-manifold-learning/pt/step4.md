# Comparar Resultados

Compare os resultados dos diferentes algoritmos de aprendizado de variedades. Visualize os dados transformados para ver como os algoritmos preservaram a estrutura subjacente dos dados.

```python
import matplotlib.pyplot as plt

# Crie um gráfico de dispersão dos dados transformados
plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y)
plt.title('Aprendizado de Variedades')
plt.xlabel('Componente 1')
plt.ylabel('Componente 2')
plt.show()
```

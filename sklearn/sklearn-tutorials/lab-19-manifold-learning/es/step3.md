# Embedding Estocástico Vecino Aleatorio Distribuido t (t-SNE)

El t-SNE es un método popular de aprendizaje de variedades que convierte las afinidades de los puntos de datos en probabilidades. Es particularmente efectivo para visualizar datos de alta dimensión.

```python
from sklearn.manifold import TSNE

# Crea una instancia del algoritmo t-SNE
tsne = TSNE(n_components=2)

# Ajusta el algoritmo a los datos y transforma los datos al espacio de baja dimensión
X_transformed = tsne.fit_transform(X)
```

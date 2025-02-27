# Análisis de Componentes Principales (PCA)

#### PCA exacto e interpretación probabilística

El Análisis de Componentes Principales (PCA, por sus siglas en inglés) se utiliza para descomponer un conjunto de datos multivariados en un conjunto de componentes ortogonales sucesivos que expliquen la mayor cantidad posible de varianza. El PCA se puede implementar utilizando la clase `PCA` de scikit-learn. El método `fit` se utiliza para aprender los componentes, y el método `transform` se puede utilizar para proyectar nuevos datos sobre estos componentes.

```python
from sklearn.decomposition import PCA

# Crea un objeto PCA con n_components como el número de componentes deseados
pca = PCA(n_components=2)

# Ajusta el modelo PCA a los datos
pca.fit(data)

# Transforma los datos proyectándolos sobre los componentes aprendidos
transformed_data = pca.transform(data)
```

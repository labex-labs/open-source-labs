# Conjunto de datos

Primero, cargaremos el conjunto de datos de diabetes utilizando la función `load_diabetes` de `sklearn.datasets`. El conjunto de datos consta de 10 variables de línea base, edad, sexo, índice de masa corporal, presión arterial media y seis mediciones de suero sanguíneo, y una medida cuantitativa de la progresión de la enfermedad un año después de la línea base.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
X.head()
```

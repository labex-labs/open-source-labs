# Cargar datos

Cargaremos el conjunto de datos de dígitos y aplanaremos las imágenes en vectores. Cada imagen de 8 por 8 píxeles debe transformarse en un vector de 64 píxeles. De este modo, obtendremos una matriz de datos final de forma `(n_imagenes, n_píxeles)`. También dividiremos los datos en un conjunto de entrenamiento y un conjunto de prueba de tamaño igual.

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

n_samples = len(digits.images)
X = digits.images.reshape((n_samples, -1))
y = digits.target == 8

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```

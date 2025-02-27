# Cargar el conjunto de datos y dividir los datos

Primero, cargaremos el conjunto de datos de dígitos utilizando la biblioteca Scikit-Learn. Este conjunto de datos consta de imágenes de 8x8 de dígitos del 0 al 9. Cada imagen se representa como una matriz de 64 características. Dividiremos los datos en variables de características y objetivo.

```python
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.images.reshape((len(digits.images), -1))
y = digits.target
```

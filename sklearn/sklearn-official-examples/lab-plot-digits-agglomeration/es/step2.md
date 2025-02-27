# Cargar el conjunto de datos

En este paso, cargaremos el conjunto de datos de dígitos de scikit-learn. Este conjunto de datos contiene imágenes de dígitos manuscritos del 0 al 9.

```python
digits = datasets.load_digits()
images = digits.images
X = np.reshape(images, (len(images), -1))
```

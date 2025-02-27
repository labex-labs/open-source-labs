# Redimensionando los Datos

A veces, los datos pueden no estar inicialmente en la forma requerida por scikit-learn. En tales casos, necesitamos preprocesar los datos para transformarlos en la forma `(n_muestras, n_características)`. Un ejemplo de redimensionamiento de datos es el conjunto de datos de dígitos, que consta de 1797 imágenes de 8x8 de dígitos escritos a mano:

```python
digits = datasets.load_digits()
print(digits.images.shape)
```

Salida:

```
(1797, 8, 8)
```

Para utilizar este conjunto de datos con scikit-learn, necesitamos redimensionar cada imagen de 8x8 en un vector de características de longitud 64:

```python
data = digits.images.reshape((digits.images.shape[0], -1))
```

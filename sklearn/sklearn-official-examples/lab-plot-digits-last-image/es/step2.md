# Visualizando el conjunto de datos

Para entender mejor el conjunto de datos, podemos visualizar una imagen de muestra utilizando matplotlib. El siguiente código muestra el último dígito del conjunto de datos:

```python
import matplotlib.pyplot as plt

# Muestra el último dígito
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
```

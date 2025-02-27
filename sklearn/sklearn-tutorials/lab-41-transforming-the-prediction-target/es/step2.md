# Binarización de múltiples etiquetas

La binarización de múltiples etiquetas es el proceso de convertir una colección de colecciones de etiquetas en un formato indicador. Esto se puede lograr utilizando la clase `MultiLabelBinarizer`.

```python
from sklearn.preprocessing import MultiLabelBinarizer

# Define una lista de colecciones de etiquetas
y = [[2, 3, 4], [2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2]]

# Crea una instancia de MultiLabelBinarizer y ajusta y transforma la lista de colecciones
MultiLabelBinarizer().fit_transform(y)
```

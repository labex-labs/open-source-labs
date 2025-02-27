# Binarización de etiquetas

La binarización de etiquetas es el proceso de convertir etiquetas de múltiples clases en una matriz indicadora binaria. Se puede lograr utilizando la clase `LabelBinarizer`.

```python
from sklearn import preprocessing

# Crea una instancia de LabelBinarizer
lb = preprocessing.LabelBinarizer()

# Ajusta el LabelBinarizer a una lista de etiquetas de múltiples clases
lb.fit([1, 2, 6, 4, 2])

# Obtiene las clases aprendidas por el LabelBinarizer
lb.classes_

# Transforma una lista de etiquetas de múltiples clases en una matriz indicadora binaria
lb.transform([1, 6])
```

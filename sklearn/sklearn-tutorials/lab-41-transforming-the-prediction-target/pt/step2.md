# Binarização de Rótulos Multi-Etiquetas

A binarização de rótulos multi-etiquetas é o processo de converter uma coleção de coleções de rótulos em um formato indicador. Isso pode ser alcançado usando a classe `MultiLabelBinarizer`.

```python
from sklearn.preprocessing import MultiLabelBinarizer

# Defina uma lista de coleções de rótulos
y = [[2, 3, 4], [2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2]]

# Crie uma instância de MultiLabelBinarizer e aplique fit_transform na lista de coleções
MultiLabelBinarizer().fit_transform(y)
```

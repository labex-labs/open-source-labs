# Carregar Dados

Usaremos o conjunto de dados iris do scikit-learn. O conjunto de dados contém 150 amostras, cada uma com quatro características e uma etiqueta de destino.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names
```

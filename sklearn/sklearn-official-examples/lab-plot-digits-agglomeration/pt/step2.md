# Carregar Conjunto de Dados

Neste passo, carregaremos o conjunto de dados de dígitos do scikit-learn. Este conjunto de dados contém imagens de dígitos manuscritos de 0 a 9.

```python
digits = datasets.load_digits()
images = digits.images
X = np.reshape(images, (len(images), -1))
```

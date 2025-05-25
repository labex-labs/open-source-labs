# Carregar o Conjunto de Dados e Dividir os Dados

Primeiro, carregaremos o conjunto de dados de dígitos usando a biblioteca Scikit-Learn. Este conjunto de dados consiste em imagens 8x8 de dígitos de 0 a 9. Cada imagem é representada como um array de 64 características. Dividiremos os dados em características e variáveis-alvo.

```python
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.images.reshape((len(digits.images), -1))
y = digits.target
```

# Carregar Dados

Vamos carregar o conjunto de dados de dígitos e achatá-los em vetores. Cada imagem de 8 por 8 pixels precisa ser transformada em um vetor de 64 pixels. Assim, obteremos um array de dados final com forma `(n_imagens, n_pixels)`. Também dividiremos os dados em um conjunto de treinamento e um conjunto de teste de tamanho igual.

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

n_samples = len(digits.images)
X = digits.images.reshape((n_samples, -1))
y = digits.target == 8

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```

# Carregar e Preparar o Conjunto de Dados

Carregamos o conjunto de dados dos dígitos e o preparamos para o agrupamento, extraindo os dados e as etiquetas alvo. Também definimos a semente aleatória para zero, garantindo a reprodutibilidade.

```python
digits = datasets.load_digits()
X, y = digits.data, digits.target
n_samples, n_features = X.shape
np.random.seed(0)
```

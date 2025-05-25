# Carregar Conjunto de Dados e Definir Parâmetros para GridSearchCV

Carregaremos o conjunto de dados de dígitos e definiremos os parâmetros para GridSearchCV. Definiremos os parâmetros para o truncamento do PCA e a regularização do classificador.

```python
X_digits, y_digits = datasets.load_digits(return_X_y=True)

param_grid = {
    "pca__n_components": [5, 15, 30, 45, 60],
    "logistic__C": np.logspace(-4, 4, 4),
}
```

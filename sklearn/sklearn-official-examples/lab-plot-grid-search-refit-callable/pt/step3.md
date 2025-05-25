# Carregar Dados e Definir Pipeline

Vamos carregar o conjunto de dados de dígitos do scikit-learn e definir um pipeline composto por PCA e LinearSVC.

```python
pipe = Pipeline(
    [
        ("reduce_dim", PCA(random_state=42)),
        ("classify", LinearSVC(random_state=42, C=0.01, dual="auto")),
    ]
)

X, y = load_digits(return_X_y=True)
```

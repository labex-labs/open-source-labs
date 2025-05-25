# Gerar Dados

Vamos gerar dados de amostra usando a função `make_blobs` da biblioteca `sklearn.datasets`. Esta função gera blobs gaussianos isotrópicos para agrupamento.

```python
X, y = make_blobs(
    n_samples=500,
    n_features=2,
    centers=4,
    cluster_std=1,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=1,
)  # Para reprodutibilidade
```

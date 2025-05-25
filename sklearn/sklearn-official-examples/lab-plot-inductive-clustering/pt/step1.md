# Gerar Dados de Treino

Neste passo, geraremos alguns dados de treino a partir do agrupamento. Usaremos a função `make_blobs` da biblioteca scikit-learn para gerar 5000 amostras com 3 clusters com diferentes desvios-padrão e centros.

```python
X, y = make_blobs(
    n_samples=5000,
    cluster_std=[1.0, 1.0, 0.5],
    centers=[(-5, -5), (0, 0), (5, 5)],
    random_state=42,
)
```

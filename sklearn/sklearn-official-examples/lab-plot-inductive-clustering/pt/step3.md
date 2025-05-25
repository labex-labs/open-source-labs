# Gerar Novas Amostras

Neste passo, geraremos novas amostras e as plotaremos juntamente com o conjunto de dados original. Usaremos novamente a função `make_blobs` para gerar 10 novas amostras.

```python
X_new, y_new = make_blobs(
    n_samples=10, centers=[(-7, -1), (-2, 4), (3, 6)], random_state=42
)
```

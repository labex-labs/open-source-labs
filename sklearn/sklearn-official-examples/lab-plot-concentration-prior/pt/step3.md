# Definir Parâmetros para o Conjunto de Dados de Brinquedo

Neste passo, definimos os parâmetros para o conjunto de dados de brinquedo, incluindo o estado aleatório, o número de componentes, o número de características, as cores, as covariâncias, as amostras e as médias.

```python
random_state, n_components, n_features = 2, 3, 2
colors = np.array(["#0072B2", "#F0E442", "#D55E00"])
covars = np.array(
    [[[0.7, 0.0], [0.0, 0.1]], [[0.5, 0.0], [0.0, 0.1]], [[0.5, 0.0], [0.0, 0.1]]]
)
samples = np.array([200, 500, 200])
means = np.array([[0.0, -0.70], [0.0, 0.0], [0.0, 0.70]])
```

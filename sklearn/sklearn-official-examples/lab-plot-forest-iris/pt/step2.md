# Definir Parâmetros

Neste passo, definiremos os parâmetros necessários para traçar as superfícies de decisão no conjunto de dados iris.

```python
# Parâmetros
n_classes = 3
n_estimators = 30
cmap = plt.cm.RdYlBu
plot_step = 0.02  # largura do passo fina para os contornos da superfície de decisão
plot_step_coarser = 0.5  # larguras dos passos para palpites grosseiros do classificador
RANDOM_SEED = 13  # fixa a semente em cada iteração
```

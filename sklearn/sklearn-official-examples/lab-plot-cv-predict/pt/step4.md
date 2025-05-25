# Visualizar Erros de Predição

Usaremos `PredictionErrorDisplay` do scikit-learn para visualizar os erros de previsão. Iremos plotar os valores reais versus os valores preditos, bem como os resíduos versus os valores preditos.

```python
import matplotlib.pyplot as plt
from sklearn.metrics import PredictionErrorDisplay

fig, axs = plt.subplots(ncols=2, figsize=(8, 4))
PredictionErrorDisplay.from_predictions(
    y,
    y_pred=y_pred,
    kind="actual_vs_predicted",
    subsample=100,
    ax=axs[0],
    random_state=0,
)
axs[0].set_title("Valores Reais vs. Valores Preditos")
PredictionErrorDisplay.from_predictions(
    y,
    y_pred=y_pred,
    kind="residual_vs_predicted",
    subsample=100,
    ax=axs[1],
    random_state=0,
)
axs[1].set_title("Resíduos vs. Valores Preditos")
fig.suptitle("Plotando previsões com validação cruzada")
plt.tight_layout()
plt.show()
```

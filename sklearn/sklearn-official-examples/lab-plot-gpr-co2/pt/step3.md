# Ajustamento e Extrapulação do Modelo

Agora, estamos prontos para usar um regressor de processo gaussiano e ajustar os dados disponíveis. Para seguir o exemplo da literatura, subtrairemos a média do alvo. Criaremos dados sintéticos de 1958 até o mês atual e usaremos o processo gaussiano para prever nos dados de treinamento para inspecionar a adequação do ajuste e dados futuros para ver a extrapolação feita pelo modelo.

```python
from sklearn.gaussian_process import GaussianProcessRegressor
import datetime
import numpy as np
import matplotlib.pyplot as plt

y_mean = y.mean()
gaussian_process = GaussianProcessRegressor(kernel=co2_kernel, normalize_y=False)
gaussian_process.fit(X, y - y_mean)

today = datetime.datetime.now()
current_month = today.year + today.month / 12
X_test = np.linspace(start=1958, stop=current_month, num=1_000).reshape(-1, 1)
mean_y_pred, std_y_pred = gaussian_process.predict(X_test, return_std=True)
mean_y_pred += y_mean

plt.plot(X, y, color="black", linestyle="dashed", label="Medidas")
plt.plot(X_test, mean_y_pred, color="tab:blue", alpha=0.4, label="Processo Gaussiano")
plt.fill_between(
    X_test.ravel(),
    mean_y_pred - std_y_pred,
    mean_y_pred + std_y_pred,
    color="tab:blue",
    alpha=0.2,
)
plt.legend()
plt.xlabel("Ano")
plt.ylabel("Média mensal da concentração de CO$_2$ (ppm)")
plt.title(
    "Medidas de média mensal de amostras de ar\ndo Observatório Mauna Loa"
)
plt.show()
```

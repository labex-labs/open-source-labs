# Limitações de um modelo linear simples

Ajustamos um modelo Ridge e verificamos as previsões deste modelo no nosso conjunto de dados.

```python
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

ridge = Ridge().fit(training_data, training_noisy_target)

plt.plot(data, target, label="Sinal verdadeiro", linewidth=2)
plt.scatter(
    training_data,
    training_noisy_target,
    color="black",
    label="Medições ruidosas",
)
plt.plot(data, ridge.predict(data), label="Regressão Ridge")
plt.legend()
plt.xlabel("Dados")
plt.ylabel("Alvo")
_ = plt.title("Limitação de um modelo linear como o ridge")
```

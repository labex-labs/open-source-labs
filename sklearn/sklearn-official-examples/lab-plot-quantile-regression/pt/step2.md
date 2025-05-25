# Visualização dos Conjuntos de Dados

Vamos visualizar os conjuntos de dados e a distribuição dos resíduos `y - média(y)`.

```python
import matplotlib.pyplot as plt

_, axs = plt.subplots(nrows=2, ncols=2, figsize=(15, 11), sharex="row", sharey="row")

axs[0, 0].plot(x, y_true_mean, label="Média Verdadeira")
axs[0, 0].scatter(x, y_normal, color="black", alpha=0.5, label="Observações")
axs[1, 0].hist(y_true_mean - y_normal, edgecolor="black")

axs[0, 1].plot(x, y_true_mean, label="Média Verdadeira")
axs[0, 1].scatter(x, y_pareto, color="black", alpha=0.5, label="Observações")
axs[1, 1].hist(y_true_mean - y_pareto, edgecolor="black")

axs[0, 0].set_title("Conjunto de dados com alvos distribuídos normalmente heterocedásticos")
axs[0, 1].set_title("Conjunto de dados com alvo distribuído de forma assimétrica de Pareto")
axs[1, 0].set_title(
    "Distribuição dos resíduos para alvos distribuídos normalmente heterocedásticos"
)
axs[1, 1].set_title("Distribuição dos resíduos para alvo distribuído assimétricamente de Pareto")
axs[0, 0].legend()
axs[0, 1].legend()
axs[0, 0].set_ylabel("y")
axs[1, 0].set_ylabel("Contagens")
axs[0, 1].set_xlabel("x")
axs[0, 0].set_xlabel("x")
axs[1, 0].set_xlabel("Resíduos")
_ = axs[1, 1].set_xlabel("Resíduos")
```

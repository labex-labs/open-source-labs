# Plotando Histogramas e Núcleos

Primeiro, plotamos histogramas e núcleos para demonstrar a diferença entre os dois. Usaremos uma estimativa de densidade de núcleo gaussiana para mostrar a diferença entre os dois. Também compararemos outros núcleos disponíveis no scikit-learn.

```python
# Importar bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.neighbors import KernelDensity

# Gerar dados
np.random.seed(1)
N = 20
X = np.concatenate(
    (np.random.normal(0, 1, int(0.3 * N)), np.random.normal(5, 1, int(0.7 * N)))
)[:, np.newaxis]
X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]
bins = np.linspace(-5, 10, 10)

# Criar figura e eixos
fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)
fig.subplots_adjust(hspace=0.05, wspace=0.05)

# Plotar histograma 1
ax[0, 0].hist(X[:, 0], bins=bins, fc="#AAAAFF", density=True)
ax[0, 0].text(-3.5, 0.31, "Histograma")

# Plotar histograma 2
ax[0, 1].hist(X[:, 0], bins=bins + 0.75, fc="#AAAAFF", density=True)
ax[0, 1].text(-3.5, 0.31, "Histograma, bins deslocados")

# Plotar KDE tophat
kde = KernelDensity(kernel="tophat", bandwidth=0.75).fit(X)
log_dens = kde.score_samples(X_plot)
ax[1, 0].fill(X_plot[:, 0], np.exp(log_dens), fc="#AAAAFF")
ax[1, 0].text(-3.5, 0.31, "Densidade do Núcleo Tophat")

# Plotar KDE gaussiano
kde = KernelDensity(kernel="gaussian", bandwidth=0.75).fit(X)
log_dens = kde.score_samples(X_plot)
ax[1, 1].fill(X_plot[:, 0], np.exp(log_dens), fc="#AAAAFF")
ax[1, 1].text(-3.5, 0.31, "Densidade do Núcleo Gaussiano")

# Plotar pontos de dados
for axi in ax.ravel():
    axi.plot(X[:, 0], np.full(X.shape[0], -0.01), "+k")
    axi.set_xlim(-4, 9)
    axi.set_ylim(-0.02, 0.34)

# Definir rótulo do eixo y para a coluna esquerda
for axi in ax[:, 0]:
    axi.set_ylabel("Densidade Normalizada")

# Definir rótulo do eixo x para a linha inferior
for axi in ax[1, :]:
    axi.set_xlabel("x")

# Mostrar o gráfico
plt.show()
```

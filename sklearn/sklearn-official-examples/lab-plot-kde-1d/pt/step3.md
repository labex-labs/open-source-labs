# Exemplo de Densidade 1D

Plotaremos um exemplo de densidade 1D com 100 amostras em uma dimensão. Compararemos três diferentes estimativas de densidade de núcleo: tophat, gaussiano e epanechnikov.

```python
# Gerar dados
N = 100
np.random.seed(1)
X = np.concatenate(
    (np.random.normal(0, 1, int(0.3 * N)), np.random.normal(5, 1, int(0.7 * N)))
)[:, np.newaxis]

X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]

true_dens = 0.3 * norm(0, 1).pdf(X_plot[:, 0]) + 0.7 * norm(5, 1).pdf(X_plot[:, 0])

# Criar figura e eixos
fig, ax = plt.subplots()

# Plotar a distribuição de entrada
ax.fill(X_plot[:, 0], true_dens, fc="black", alpha=0.2, label="distribuição de entrada")

# Definir cores e núcleos
cores = ["navy", "cornflowerblue", "darkorange"]
núcleos = ["gaussian", "tophat", "epanechnikov"]
lw = 2

# Plotar estimativas de densidade de núcleo
for cor, núcleo in zip(cores, núcleos):
    kde = KernelDensity(kernel=núcleo, bandwidth=0.5).fit(X)
    log_dens = kde.score_samples(X_plot)
    ax.plot(
        X_plot[:, 0],
        np.exp(log_dens),
        color=cor,
        lw=lw,
        linestyle="-",
        label="núcleo = '{0}'".format(núcleo),
    )

ax.text(6, 0.38, "N={0} pontos".format(N))

# Definir legenda e plotar pontos de dados
ax.legend(loc="upper left")
ax.plot(X[:, 0], -0.005 - 0.01 * np.random.random(X.shape[0]), "+k")

# Definir limites x e y
ax.set_xlim(-4, 9)
ax.set_ylim(-0.02, 0.4)

# Mostrar o gráfico
plt.show()
```

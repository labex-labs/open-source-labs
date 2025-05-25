# Plotando os Resultados do Experimento 2

Plotamos os resultados do segundo experimento utilizando a biblioteca `matplotlib`. Observamos resultados semelhantes aos do primeiro experimento: as métricas ajustadas para o acaso permanecem constantemente próximas de zero, enquanto outras métricas tendem a aumentar com rotulações mais detalhadas. A medida média V-measure de rotulação aleatória aumenta significativamente à medida que o número de clusters se aproxima do número total de amostras usadas para calcular a medida.

```python
n_samples = 100
n_clusters_range = np.linspace(2, n_samples, 10).astype(int)

plt.figure(2)

plots = []
names = []

for marker, (score_name, score_func) in zip("d^vx.,", score_funcs):
    scores = uniform_labelings_scores(score_func, n_samples, n_clusters_range)
    plots.append(
        plt.errorbar(
            n_clusters_range,
            np.median(scores, axis=1),
            scores.std(axis=1),
            alpha=0.8,
            linewidth=2,
            marker=marker,
        )[0]
    )
    names.append(score_name)

plt.title(
    "Medidas de agrupamento para 2 rotulações aleatórias uniformes\ncom número igual de clusters"
)
plt.xlabel(f"Número de clusters (Número de amostras fixo em {n_samples})")
plt.ylabel("Valor da pontuação")
plt.legend(plots, names)
plt.ylim(bottom=-0.05, top=1.05)
plt.show()
```

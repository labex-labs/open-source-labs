# Plotando os Resultados do Experimento 1

Plotamos os resultados do primeiro experimento usando as bibliotecas `matplotlib` e `seaborn`. O índice Rand satura para `n_clusters` > `n_classes`. Outras medidas não ajustadas, como a Medida V, mostram uma dependência linear entre o número de clusters e o número de amostras. Medidas ajustadas para o acaso, como ARI e AMI, exibem algumas variações aleatórias centradas em uma pontuação média de 0,0, independentemente do número de amostras e clusters.

```python
import matplotlib.pyplot as plt
import seaborn as sns

n_samples = 1000
n_classes = 10
n_clusters_range = np.linspace(2, 100, 10).astype(int)
plots = []
names = []

sns.color_palette("colorblind")
plt.figure(1)

for marker, (score_name, score_func) in zip("d^vx.,", score_funcs):
    scores = fixed_classes_uniform_labelings_scores(
        score_func, n_samples, n_clusters_range, n_classes=n_classes
    )
    plots.append(
        plt.errorbar(
            n_clusters_range,
            scores.mean(axis=1),
            scores.std(axis=1),
            alpha=0.8,
            linewidth=1,
            marker=marker,
        )[0]
    )
    names.append(score_name)

plt.title(
    "Medidas de agrupamento para rotulagem aleatória uniforme\n"
    f"contra atribuição de referência com {n_classes} classes"
)
plt.xlabel(f"Número de clusters (Número de amostras fixo em {n_samples})")
plt.ylabel("Valor da pontuação")
plt.ylim(bottom=-0.05, top=1.05)
plt.legend(plots, names, bbox_to_anchor=(0.5, 0.5))
plt.show()
```

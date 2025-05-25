# Plotar os resultados

```python
# Plotar a evolução da precisão
plt.figure()
for _, stats in sorted(cls_stats.items()):
    # Plotar a evolução da precisão com o número de exemplos
    accuracy, n_examples = zip(*stats["accuracy_history"])
    plot_accuracy(n_examples, accuracy, "exemplos de treinamento (#)")
    ax = plt.gca()
    ax.set_ylim((0.8, 1))
plt.legend(cls_names, loc="best")

plt.figure()
for _, stats in sorted(cls_stats.items()):
    # Plotar a evolução da precisão com o tempo de execução
    accuracy, runtime = zip(*stats["runtime_history"])
    plot_accuracy(runtime, accuracy, "tempo de execução (s)")
    ax = plt.gca()
    ax.set_ylim((0.8, 1))
plt.legend(cls_names, loc="best")

# Plotar os tempos de ajuste
plt.figure()
fig = plt.gcf()
cls_runtime = [stats["total_fit_time"] for cls_name, stats in sorted(cls_stats.items())]

cls_runtime.append(total_vect_time)
cls_names.append("Vectorização")
bar_colors = ["b", "g", "r", "c", "m", "y"]

ax = plt.subplot(111)
rectangles = plt.bar(range(len(cls_names)), cls_runtime, width=0.5, color=bar_colors)

ax.set_xticks(np.linspace(0, len(cls_names) - 1, len(cls_names)))
ax.set_xticklabels(cls_names, fontsize=10)
ymax = max(cls_runtime) * 1.2
ax.set_ylim((0, ymax))
ax.set_ylabel("tempo de execução (s)")
ax.set_title("Tempos de Treinamento")


def autolabel(rectangles):
    """adicionar algum texto via autolabel nos retângulos."""
    for rect in rectangles:
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2.0,
            1.05 * height,
            "%.4f" % height,
            ha="center",
            va="bottom",
        )
        plt.setp(plt.xticks()[1], rotation=30)


autolabel(rectangles)
plt.tight_layout()
plt.show()

# Plotar os tempos de previsão
plt.figure()
cls_runtime = []
cls_names = list(sorted(cls_stats.keys()))
for cls_name, stats in sorted(cls_stats.items()):
    cls_runtime.append(stats["prediction_time"])
cls_runtime.append(parsing_time)
cls_names.append("Leitura/Parse\n+Extr. de Feat.")
cls_runtime.append(vectorizing_time)
cls_names.append("Hashing\n+Vet.")

ax = plt.subplot(111)
rectangles = plt.bar(range(len(cls_names)), cls_runtime, width=0.5, color=bar_colors)

ax.set_xticks(np.linspace(0, len(cls_names) - 1, len(cls_names)))
ax.set_xticklabels(cls_names, fontsize=8)
plt.setp(plt.xticks()[1], rotation=30)
ymax = max(cls_runtime) * 1.2
ax.set_ylim((0, ymax))
ax.set_ylabel("tempo de execução (s)")
ax.set_title("Tempos de Predição (%d instâncias)" % n_test_documents)
autolabel(rectangles)
plt.tight_layout()
plt.show()
```

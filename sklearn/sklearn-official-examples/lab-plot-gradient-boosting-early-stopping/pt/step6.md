# Comparar Tempos de Ajustamento com e sem Parada Antecipada

Agora, compararemos os tempos de ajuste dos dois modelos.

```python
plt.figure(figsize=(9, 5))

bar1 = plt.bar(
    index, time_gb, bar_width, label="Sem parada antecipada", color="crimson"
)
bar2 = plt.bar(
    index + bar_width, time_gbes, bar_width, label="Com parada antecipada", color="coral"
)

max_y = np.amax(np.maximum(time_gb, time_gbes))

plt.xticks(index + bar_width, names)
plt.yticks(np.linspace(0, 1.3 * max_y, 13))

autolabel(bar1, n_gb)
autolabel(bar2, n_gbes)

plt.ylim([0, 1.3 * max_y])
plt.legend(loc="best")
plt.grid(True)

plt.xlabel("Datasets")
plt.ylabel("Tempo de Ajuste")

plt.show()
```

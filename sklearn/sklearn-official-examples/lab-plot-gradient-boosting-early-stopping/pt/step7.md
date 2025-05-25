# Comparar Pontuações com e sem Parada Antecipada

Agora, compararemos as pontuações dos dois modelos.

```python
plt.figure(figsize=(9, 5))

bar1 = plt.bar(
    index, score_gb, bar_width, label="Sem parada antecipada", color="crimson"
)
bar2 = plt.bar(
    index + bar_width, score_gbes, bar_width, label="Com parada antecipada", color="coral"
)

plt.xticks(index + bar_width, names)
plt.yticks(np.arange(0, 1.3, 0.1))

autolabel(bar1, n_gb)
autolabel(bar2, n_gbes)

plt.ylim([0, 1.3])
plt.legend(loc="best")
plt.grid(True)

plt.xlabel("Datasets")
plt.ylabel("Pontuação de Teste")

plt.show()
```

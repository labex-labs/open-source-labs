# Visualizar Resultados

Finalmente, vamos visualizar os resultados dos modelos treinados usando um gráfico de linha.

```python
fig = plt.figure()
ax = fig.add_subplot(111)

for model in models:
    name = models[model]["name"]
    times = models[model]["times"]
    accuracies = models[model]["accuracies"]
    ax.plot(times, accuracies, marker="o", label="Modelo: %s" % name)
    ax.set_xlabel("Tempo de treino (s)")
    ax.set_ylabel("Precisão de teste")
ax.legend()
fig.suptitle("Regressão Logística L1 Multinomial vs One-vs-Rest\nConjunto de Dados %s" % "20newsgroups")
fig.tight_layout()
fig.subplots_adjust(top=0.85)
run_time = timeit.default_timer() - t0
print("Tempo de execução do exemplo em %.3f s" % run_time)
plt.show()
```

# Visualizar los resultados

Finalmente, visualizaremos los resultados de los modelos entrenados utilizando un gráfico de líneas.

```python
fig = plt.figure()
ax = fig.add_subplot(111)

for model in models:
    name = models[model]["name"]
    times = models[model]["times"]
    accuracies = models[model]["accuracies"]
    ax.plot(times, accuracies, marker="o", label="Modelo: %s" % name)
    ax.set_xlabel("Tiempo de entrenamiento (s)")
    ax.set_ylabel("Precisión de prueba")
ax.legend()
fig.suptitle("Multinomial vs One-vs-Rest Logistic L1\nConjunto de datos %s" % "20newsgroups")
fig.tight_layout()
fig.subplots_adjust(top=0.85)
run_time = timeit.default_timer() - t0
print("Ejecución de ejemplo en %.3f s" % run_time)
plt.show()
```

# Gerar Grade e Plotar

Geramos uma grade de possíveis probabilidades não calibradas sobre o 2-simplex, calculamos as probabilidades calibradas correspondentes e plotamos setas para cada uma. As setas são coloridas de acordo com a probabilidade não calibrada mais alta. Isso ilustra o mapa de calibração aprendido:

```python
plt.figure(figsize=(10, 10))
# Gerar grade de valores de probabilidade
p1d = np.linspace(0, 1, 20)
p0, p1 = np.meshgrid(p1d, p1d)
p2 = 1 - p0 - p1
p = np.c_[p0.ravel(), p1.ravel(), p2.ravel()]
p = p[p[:, 2] >= 0]

# Usar os calibradores de classe para calcular as probabilidades calibradas
calibrated_classifier = cal_clf.calibrated_classifiers_[0]
prediction = np.vstack(
    [
        calibrator.predict(this_p)
        for calibrator, this_p in zip(calibrated_classifier.calibrators, p.T)
    ]
).T

# Re-normalizar as previsões calibradas para garantir que permaneçam dentro do
# simplex. Esta mesma etapa de renormalização é executada internamente pelo
# método predict de CalibratedClassifierCV em problemas multiclasse.
prediction /= prediction.sum(axis=1)[:, None]

# Plotar as mudanças nas probabilidades previstas induzidas pelos calibradores
for i in range(prediction.shape[0]):
    plt.arrow(
        p[i, 0],
        p[i, 1],
        prediction[i, 0] - p[i, 0],
        prediction[i, 1] - p[i, 1],
        head_width=1e-2,
        color=colors[np.argmax(p[i])],
    )

# Plotar os limites do simplex unitário
plt.plot([0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], "k", label="Simplex")

plt.grid(False)
for x in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    plt.plot([0, x], [x, 0], "k", alpha=0.2)
    plt.plot([0, 0 + (1 - x) / 2], [x, x + (1 - x) / 2], "k", alpha=0.2)
    plt.plot([x, x + (1 - x) / 2], [0, 0 + (1 - x) / 2], "k", alpha=0.2)

plt.title("Mapa de calibração sigmoid aprendido")
plt.xlabel("Probabilidade da classe 1")
plt.ylabel("Probabilidade da classe 2")
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)

plt.show()
```

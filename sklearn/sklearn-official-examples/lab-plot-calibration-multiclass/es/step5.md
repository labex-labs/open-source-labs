# Generar cuadrícula y graficar

Generamos una cuadrícula de probabilidades no calibradas posibles sobre el 2-simplex, calculamos las probabilidades calibradas correspondientes y graficamos flechas para cada una. Las flechas se colorean de acuerdo con la probabilidad no calibrada más alta. Esto ilustra el mapa de calibración aprendido:

```python
plt.figure(figsize=(10, 10))
# Generar cuadrícula de valores de probabilidad
p1d = np.linspace(0, 1, 20)
p0, p1 = np.meshgrid(p1d, p1d)
p2 = 1 - p0 - p1
p = np.c_[p0.ravel(), p1.ravel(), p2.ravel()]
p = p[p[:, 2] >= 0]

# Usar los tres calibradores por clase para calcular las probabilidades calibradas
calibrated_classifier = cal_clf.calibrated_classifiers_[0]
prediction = np.vstack(
    [
        calibrator.predict(this_p)
        for calibrator, this_p in zip(calibrated_classifier.calibrators, p.T)
    ]
).T

# Re-normalizar las predicciones calibradas para asegurarse de que queden dentro del
# simplex. Este mismo paso de renormalización se realiza internamente por el
# método predict de CalibratedClassifierCV en problemas multiclasificación.
prediction /= prediction.sum(axis=1)[:, None]

# Graficar los cambios en las probabilidades predichas inducidos por los calibradores
for i in range(prediction.shape[0]):
    plt.arrow(
        p[i, 0],
        p[i, 1],
        prediction[i, 0] - p[i, 0],
        prediction[i, 1] - p[i, 1],
        head_width=1e-2,
        color=colors[np.argmax(p[i])],
    )

# Graficar los límites del simplex unitario
plt.plot([0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], "k", label="Simplex")

plt.grid(False)
for x in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    plt.plot([0, x], [x, 0], "k", alpha=0.2)
    plt.plot([0, 0 + (1 - x) / 2], [x, x + (1 - x) / 2], "k", alpha=0.2)
    plt.plot([x, x + (1 - x) / 2], [0, 0 + (1 - x) / 2], "k", alpha=0.2)

plt.title("Mapa de calibración sigmoide aprendido")
plt.xlabel("Probabilidad de la clase 1")
plt.ylabel("Probabilidad de la clase 2")
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)

plt.show()
```

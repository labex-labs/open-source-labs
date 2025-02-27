# Grid generieren und plotten

Wir generieren ein Gitter von möglichen unkalibrierten Wahrscheinlichkeiten über den 2-Simplex, berechnen die entsprechenden kalibrierten Wahrscheinlichkeiten und zeichnen für jede Pfeile. Die Pfeile sind nach der höchsten unkalibrierten Wahrscheinlichkeit gefärbt. Dies veranschaulicht die gelernten Kalibrierungskarten:

```python
plt.figure(figsize=(10, 10))
# Generiere Gitter von Wahrscheinlichkeitswerten
p1d = np.linspace(0, 1, 20)
p0, p1 = np.meshgrid(p1d, p1d)
p2 = 1 - p0 - p1
p = np.c_[p0.ravel(), p1.ravel(), p2.ravel()]
p = p[p[:, 2] >= 0]

# Verwende die drei klassenspezifischen Kalibrierer, um kalibrierte Wahrscheinlichkeiten zu berechnen
kalibrierter_klassifikator = cal_clf.calibrated_classifiers_[0]
vorhersage = np.vstack(
    [
        kalibrierer.predict(this_p)
        for kalibrierer, this_p in zip(kalibrierter_klassifikator.calibrators, p.T)
    ]
).T

# Normalisiere die kalibrierten Vorhersagen erneut, um sicherzustellen, dass sie innerhalb des
# Simplex bleiben. Dieser gleiche Normalisierungsschritt wird intern von der
# predict-Methode von CalibratedClassifierCV bei Mehrklassenproblemen durchgeführt.
vorhersage /= vorhersage.sum(axis=1)[:, None]

# Zeichne die Änderungen der vorhergesagten Wahrscheinlichkeiten, die durch die Kalibrierer verursacht werden
for i in range(vorhersage.shape[0]):
    plt.arrow(
        p[i, 0],
        p[i, 1],
        vorhersage[i, 0] - p[i, 0],
        vorhersage[i, 1] - p[i, 1],
        head_width=1e-2,
        color=colors[np.argmax(p[i])],
    )

# Zeichne die Grenzen des Einheits-Simplex
plt.plot([0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], "k", label="Simplex")

plt.grid(False)
for x in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    plt.plot([0, x], [x, 0], "k", alpha=0.2)
    plt.plot([0, 0 + (1 - x) / 2], [x, x + (1 - x) / 2], "k", alpha=0.2)
    plt.plot([x, x + (1 - x) / 2], [0, 0 + (1 - x) / 2], "k", alpha=0.2)

plt.title("Gelernte Sigmoid-Kalibrierungskarte")
plt.xlabel("Wahrscheinlichkeit Klasse 1")
plt.ylabel("Wahrscheinlichkeit Klasse 2")
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)

plt.show()
```

# Générer une grille et tracer

Nous générons une grille de probabilités non étalonnées possibles sur le 2-simplex, calculons les probabilités étalonnées correspondantes et traçons des flèches pour chacune. Les flèches sont colorées selon la plus haute probabilité non étalonnée. Cela illustre la carte d'étalonnage apprise :

```python
plt.figure(figsize=(10, 10))
# Générer une grille de valeurs de probabilité
p1d = np.linspace(0, 1, 20)
p0, p1 = np.meshgrid(p1d, p1d)
p2 = 1 - p0 - p1
p = np.c_[p0.ravel(), p1.ravel(), p2.ravel()]
p = p[p[:, 2] >= 0]

# Utiliser les trois étalonneurs par classe pour calculer les probabilités étalonnées
calibrated_classifier = cal_clf.calibrated_classifiers_[0]
prediction = np.vstack(
    [
        calibrator.predict(this_p)
        for calibrator, this_p in zip(calibrated_classifier.calibrators, p.T)
    ]
).T

# Renormaliser les prédictions étalonnées pour vous assurer qu'elles restent à l'intérieur du
# simplex. Cette même étape de renormalisation est effectuée internement par la
# méthode predict de CalibratedClassifierCV pour les problèmes multiclasse.
prediction /= prediction.sum(axis=1)[:, None]

# Tracer les changements dans les probabilités prédites induits par les étalonneurs
for i in range(prediction.shape[0]):
    plt.arrow(
        p[i, 0],
        p[i, 1],
        prediction[i, 0] - p[i, 0],
        prediction[i, 1] - p[i, 1],
        head_width=1e-2,
        color=colors[np.argmax(p[i])],
    )

# Tracer les limites du simplex unitaire
plt.plot([0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], "k", label="Simplex")

plt.grid(False)
for x in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    plt.plot([0, x], [x, 0], "k", alpha=0.2)
    plt.plot([0, 0 + (1 - x) / 2], [x, x + (1 - x) / 2], "k", alpha=0.2)
    plt.plot([x, x + (1 - x) / 2], [0, 0 + (1 - x) / 2], "k", alpha=0.2)

plt.title("Carte d'étalonnage sigmoïde apprise")
plt.xlabel("Probabilité de la classe 1")
plt.ylabel("Probabilité de la classe 2")
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)

plt.show()
```

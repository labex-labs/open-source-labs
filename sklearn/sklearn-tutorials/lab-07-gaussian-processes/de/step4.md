# GPC-Beispiele

Probabilistische Vorhersagen mit GPC: In diesem Beispiel wird die vorhergesagte Wahrscheinlichkeit der GPC mit verschiedenen Auswahlmöglichkeiten von Hyperparametern veranschaulicht.

```python
# Erstellen eines GPC-Modells mit einem RBF-Kern
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Anpassen des Modells an die Trainingsdaten
model.fit(X_train, y_train)

# Vorhersagen der Klassenwahrscheinlichkeiten der Testdaten
y_prob = model.predict_proba(X_test)
```

Veranschaulichung von GPC auf dem XOR-Datensatz: In diesem Beispiel wird die Verwendung von GPC auf dem XOR-Datensatz demonstriert. Wir vergleichen die Ergebnisse der Verwendung eines stationären, isotropen Kerns (RBF) und eines nicht-stationären Kerns (DotProduct).

```python
# Erstellen von GPC-Modellen mit verschiedenen Kernen
isotropischer_kernel = RBF(length_scale=1.0)
nicht-stationärer_kernel = DotProduct(sigma_0=1.0)

# Anpassen der Modelle an den XOR-Datensatz
isotropisches_model = GaussianProcessClassifier(kernel=isotropischer_kernel)
nicht-stationäres_model = GaussianProcessClassifier(kernel=nicht-stationärer_kernel)
isotropisches_model.fit(X_xor, y_xor)
nicht-stationäres_model.fit(X_xor, y_xor)

# Vorhersagen mit den trainierten Modellen
isotropische_y_pred = isotropisches_model.predict(X_test)
nicht-stationäre_y_pred = nicht-stationäres_model.predict(X_test)
```

GPC auf dem iris-Datensatz: In diesem Beispiel wird GPC auf dem iris-Datensatz mit einem isotropen RBF-Kern und einem anisotropen RBF-Kern veranschaulicht. Es wird gezeigt, wie verschiedene Auswahlmöglichkeiten von Hyperparametern die vorhergesagte Wahrscheinlichkeit beeinflussen können.

```python
# Erstellen von GPC-Modellen mit verschiedenen Kernen und Anpassen an den iris-Datensatz
isotropischer_kernel = RBF(length_scale=1.0)
anisotropischer_kernel = RBF(length_scale=[1.0, 2.0])
isotropisches_model = GaussianProcessClassifier(kernel=isotropischer_kernel)
anisotropisches_model = GaussianProcessClassifier(kernel=anisotropischer_kernel)
isotropisches_model.fit(X_train, y_train)
anisotropisches_model.fit(X_train, y_train)

# Vorhersagen der Klassenwahrscheinlichkeiten
isotropische_y_prob = isotropisches_model.predict_proba(X_test)
anisotropische_y_prob = anisotropisches_model.predict_proba(X_test)
```

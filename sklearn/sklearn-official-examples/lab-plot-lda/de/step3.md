# Klassifizierer trainieren und testen

Wir werden jeden Klassifizierer trainieren und testen, um zu sehen, wie sie auf den generierten Daten performen. Wir werden diesen Prozess mehrmals wiederholen, um einen durchschnittlichen Genauigkeitsscore zu erhalten.

```python
n_train = 20  # Stichproben für das Training
n_test = 200  # Stichproben für das Testen
n_averages = 50  # Wie oft die Klassifizierung wiederholt werden soll
n_features_max = 75  # Maximale Anzahl von Merkmalen
step = 4  # Schrittweite für die Berechnung

acc_clf1, acc_clf2, acc_clf3 = [], [], []
n_features_range = range(1, n_features_max + 1, step)

for n_features in n_features_range:
    score_clf1, score_clf2, score_clf3 = 0, 0, 0
    for _ in range(n_averages):
        X, y = generate_data(n_train, n_features)

        clf1.fit(X, y)
        clf2.fit(X, y)
        clf3.fit(X, y)

        X, y = generate_data(n_test, n_features)
        score_clf1 += clf1.score(X, y)
        score_clf2 += clf2.score(X, y)
        score_clf3 += clf3.score(X, y)

    acc_clf1.append(score_clf1 / n_averages)
    acc_clf2.append(score_clf2 / n_averages)
    acc_clf3.append(score_clf3 / n_averages)
```

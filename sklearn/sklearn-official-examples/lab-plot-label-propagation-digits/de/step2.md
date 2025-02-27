# Daten für halbsupervisioniertes Lernen vorbereiten

Wir wählen 340 Stichproben aus, und nur 40 dieser Stichproben sind mit einem bekannten Label (Kategorie) verknüpft. Wir speichern die Indizes der anderen 300 Stichproben, für die wir die Labels nicht kennen sollen. Anschließend mischen wir die Labels so, dass die ungelabelten Stichproben mit -1 markiert werden.

```python
X = digits.data[indices[:340]]
y = digits.target[indices[:340]]

n_total_samples = len(y)
n_labeled_points = 40

indices = np.arange(n_total_samples)

unlabeled_set = indices[n_labeled_points:]

y_train = np.copy(y)
y_train[unlabeled_set] = -1
```

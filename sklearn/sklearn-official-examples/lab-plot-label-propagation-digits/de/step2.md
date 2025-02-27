# Daten für das halbüberwachte Lernen vorbereiten

Wir wählen 340 Proben aus, und nur 40 dieser Proben sind mit einem bekannten Label assoziiert. Wir speichern die Indizes der anderen 300 Proben, für die wir nicht wissen sollen, was ihr Label ist. Anschließend mischen wir die Labels, sodass die unmarkierten Proben mit -1 markiert werden.

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
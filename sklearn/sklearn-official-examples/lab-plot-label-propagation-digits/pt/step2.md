# Preparar Dados para Aprendizado Semi-Supervisionado

Selecionamos 340 amostras, e apenas 40 dessas amostras estão associadas a um rótulo conhecido. Armazenamos os índices das outras 300 amostras para as quais não deveríamos conhecer seus rótulos. Em seguida, embaralhamos os rótulos para que as amostras não rotuladas sejam marcadas com -1.

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

# Erstellen eines gewichteten Datensatzes

Wir erstellen einen gewichteten Datensatz mit der numpy-Bibliothek. Wir generieren 20 Punkte mit zufälligen Werten und weisen den letzten 10 Proben einen größeren Gewicht zu.

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
sample_weight = 100 * np.abs(np.random.randn(20))
sample_weight[:10] *= 10
```

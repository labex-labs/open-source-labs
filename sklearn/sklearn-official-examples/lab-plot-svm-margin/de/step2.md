# Daten generieren

Wir generieren 40 trennbare Punkte mit der Funktion `random.randn` von numpy. Die ersten 20 Punkte haben einen Mittelwert von [-2, -2], und die nächsten 20 Punkte haben einen Mittelwert von [2, 2]. Anschließend weisen wir den ersten 20 Punkten ein Klassenlabel von 0 und den nächsten 20 Punkten ein Klassenlabel von 1 zu.

```python
np.random.seed(0)
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
Y = [0] * 20 + [1] * 20
```

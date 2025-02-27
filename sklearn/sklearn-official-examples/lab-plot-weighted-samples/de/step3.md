# Stichprobengewichte erstellen

Wir werden zwei Sets von Stichprobengewichten erstellen. Das erste Set von Stichprobengewichten wird für alle Punkte konstant sein, und das zweite Set von Stichprobengewichten wird für einige Ausreißer größer sein.

```python
sample_weight_last_ten = abs(np.random.randn(len(X)))
sample_weight_constant = np.ones(len(X))
sample_weight_last_ten[15:] *= 5
sample_weight_last_ten[9] *= 15
```

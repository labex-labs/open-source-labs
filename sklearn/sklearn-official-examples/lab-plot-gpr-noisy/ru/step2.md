# Визуализация данных

В этом шаге мы визуализируем сгенерированные данные.

```python
import matplotlib.pyplot as plt

plt.plot(X, y, label="Expected signal")
plt.legend()
plt.xlabel("X")
_ = plt.ylabel("y")
```

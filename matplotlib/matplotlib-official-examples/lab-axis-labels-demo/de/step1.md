# Matplotlib importieren und einen Streudiagramm erstellen

Wir beginnen, indem wir Matplotlib importieren und ein Streudiagramm erstellen.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sc = ax.scatter([1, 2], [1, 2], c=[1, 2])
```

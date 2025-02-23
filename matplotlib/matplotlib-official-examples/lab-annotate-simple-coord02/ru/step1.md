# Импорт Matplotlib

Прежде чем мы сможем начать добавлять аннотации к графикам с использованием Matplotlib, мы должны сначала импортировать библиотеку. В этом шаге мы импортируем Matplotlib и создаем простой график, который будем использовать для аннотации.

```python
import matplotlib.pyplot as plt

# Create a simple plot
fig, ax = plt.subplots()
ax.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.show()
```

# Визуализация результатов

Наконец, мы можем построить график предсказанных значений против фактических значений, чтобы визуализировать, насколько хорошо модель подходит к данным.

```python
import matplotlib.pyplot as plt

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
```

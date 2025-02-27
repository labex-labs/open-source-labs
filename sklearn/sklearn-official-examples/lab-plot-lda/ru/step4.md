# Визуализация результатов

Наконец, мы построим график точности классификации для каждого классификатора в зависимости от числа признаков. Для создания графика мы будем использовать matplotlib.

```python
import matplotlib.pyplot as plt

features_samples_ratio = np.array(n_features_range) / n_train

plt.plot(
    features_samples_ratio,
    acc_clf1,
    linewidth=2,
    label="LDA",
    color="gold",
    linestyle="solid",
)
plt.plot(
    features_samples_ratio,
    acc_clf2,
    linewidth=2,
    label="LDA with Ledoit Wolf",
    color="navy",
    linestyle="dashed",
)
plt.plot(
    features_samples_ratio,
    acc_clf3,
    linewidth=2,
    label="LDA with OAS",
    color="red",
    linestyle="dotted",
)

plt.xlabel("n_features / n_samples")
plt.ylabel("Classification accuracy")

plt.legend(loc="lower left")
plt.ylim((0.65, 1.0))
plt.suptitle(
    "LDA (Linear Discriminant Analysis) vs. "
    + "\n"
    + "LDA with Ledoit Wolf vs. "
    + "\n"
    + "LDA with OAS (1 discriminative feature)"
)
plt.show()
```

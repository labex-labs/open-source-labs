# Einschränkungen eines einfachen linearen Modells

Wir trainieren ein Ridge-Modell und überprüfen die Vorhersagen dieses Modells auf unserem Datensatz.

```python
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

ridge = Ridge().fit(training_data, training_noisy_target)

plt.plot(data, target, label="True signal", linewidth=2)
plt.scatter(
    training_data,
    training_noisy_target,
    color="black",
    label="Noisy measurements",
)
plt.plot(data, ridge.predict(data), label="Ridge regression")
plt.legend()
plt.xlabel("data")
plt.ylabel("target")
_ = plt.title("Limitation of a linear model such as ridge")
```

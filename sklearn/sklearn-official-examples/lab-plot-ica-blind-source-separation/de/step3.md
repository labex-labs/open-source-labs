# Ergebnisse grafisch darstellen

Wir werden das ursprüngliche gemischte Signal, die ursprünglichen unabhängigen Quellen, die von ICA geschätzten Quellen und die von PCA geschätzten Quellen grafisch darstellen.

```python
import matplotlib.pyplot as plt

plt.figure()

models = [X, S, S_, H]
names = [
    "Beobachtungen (gemischtes Signal)",
    "Wahre Quellen",
    "Durch ICA wiederhergestellte Signale",
    "Durch PCA wiederhergestellte Signale",
]
colors = ["rot", "stahlblau", "orange"]

for ii, (model, name) in enumerate(zip(models, names), 1):
    plt.subplot(4, 1, ii)
    plt.title(name)
    for sig, color in zip(model.T, colors):
        plt.plot(sig, color=color)

plt.tight_layout()
plt.show()
```

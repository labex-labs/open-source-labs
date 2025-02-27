# Tracer la trajectoire de régularisation

Nous allons tracer la trajectoire de régularisation en utilisant les coefficients des modèles entraînés. Les coefficients seront tracés en fonction du logarithme de la force de régularisation. Sur le côté gauche de la figure (régulariseurs forts), tous les coefficients sont exactement égaux à 0. Lorsque la régularisation devient progressivement moins stricte, les coefficients peuvent prendre des valeurs non nulles les uns après les autres.

```python
import matplotlib.pyplot as plt

plt.plot(np.log10(cs), coefs_, marker="o")
ymin, ymax = plt.ylim()
plt.xlabel("log(C)")
plt.ylabel("Coefficients")
plt.title("Logistic Regression Path")
plt.axis("tight")
plt.show()
```

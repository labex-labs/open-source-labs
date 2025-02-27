# Visualiser les résultats

Enfin, nous pouvons tracer les valeurs prédites en fonction des valeurs réelles pour visualiser la qualité de l'ajustement du modèle aux données.

```python
import matplotlib.pyplot as plt

# Tracer les sorties
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
```

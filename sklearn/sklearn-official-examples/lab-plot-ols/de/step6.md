# Visualisiere die Ergebnisse

Schließlich können wir die vorhergesagten Werte gegen die tatsächlichen Werte aufzeichnen, um zu visualisieren, wie gut das Modell die Daten anpasst.

```python
import matplotlib.pyplot as plt

# Zeichne die Ausgaben
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
```

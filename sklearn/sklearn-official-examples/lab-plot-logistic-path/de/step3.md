# Zeichne den Regularisierungspfad

Wir werden den Regularisierungspfad zeichnen, indem wir die Koeffizienten der trainierten Modelle verwenden. Die Koeffizienten werden gegen den Logarithmus der Regularisierungsstärke aufgetragen. Auf der linken Seite der Abbildung (starke Regularisatoren) sind alle Koeffizienten genau 0. Wenn die Regularisierung zunehmend lockerer wird, können die Koeffizienten nacheinander nicht-nulle Werte annehmen.

```python
import matplotlib.pyplot as plt

plt.plot(np.log10(cs), coefs_, marker="o")
ymin, ymax = plt.ylim()
plt.xlabel("log(C)")
plt.ylabel("Koeffizienten")
plt.title("Logistischer Regressionspfad")
plt.axis("tight")
plt.show()
```

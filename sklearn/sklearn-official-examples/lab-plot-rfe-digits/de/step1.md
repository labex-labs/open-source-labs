# Lade den Datensatz und teile die Daten auf

Zunächst werden wir den Digits-Datensatz mit der Scikit-Learn-Bibliothek laden. Dieser Datensatz besteht aus 8x8-Bildern von Ziffern von 0 bis 9. Jedes Bild wird als Array von 64 Features dargestellt. Wir werden die Daten in Features und Zielvariablen aufteilen.

```python
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.images.reshape((len(digits.images), -1))
y = digits.target
```

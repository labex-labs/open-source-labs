# Visualisierung des Datasets

Um das Dataset besser zu verstehen, können wir ein Beispielbild mit matplotlib visualisieren. Der folgende Code zeigt die letzte Zahl im Dataset an:

```python
import matplotlib.pyplot as plt

# Zeige die letzte Zahl an
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
```

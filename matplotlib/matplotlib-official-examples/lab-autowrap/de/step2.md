# Erstellen eines einfachen Graphen

Lassen Sie uns beginnen, indem wir einen einfachen Graphen mit einem Textelement erstellen. Fügen Sie im Python-Skript folgenden Code hinzu:

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(5, 5, "Hello, Matplotlib!", ha='center')
plt.show()
```

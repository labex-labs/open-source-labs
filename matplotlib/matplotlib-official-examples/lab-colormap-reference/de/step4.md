# Umkehren von Farbskalen

Matplotlib bietet die Möglichkeit, eine Farbskala umzukehren, indem man `_r` an den Namen der Farbskala anhängt.

```python
import matplotlib.pyplot as plt

# Erzeuge ein Diagramm mit der umgekehrten Farbskala 'viridis'
plt.imshow(data, cmap='viridis_r')
plt.colorbar()
```

# Creando una gráfica básica

Comencemos creando una gráfica básica con un elemento de texto. En su script de Python, agregue el siguiente código:

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(5, 5, "Hello, Matplotlib!", ha='center')
plt.show()
```

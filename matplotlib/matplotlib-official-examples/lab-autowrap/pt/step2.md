# Criando um Gráfico Básico

Vamos começar criando um gráfico básico com um elemento de texto. Em seu script Python, adicione o seguinte código:

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(5, 5, "Hello, Matplotlib!", ha='center')
plt.show()
```

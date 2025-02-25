# Créer un graphe linéaire simple

Commençons par créer un graphe linéaire simple. Dans cet exemple, nous allons tracer les fonctions sinus et cosinus sur l'intervalle [0, 2π].

```python
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin')
plt.plot(x, y2, label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fonctions sinus et cosinus')
plt.legend()
plt.show()
```

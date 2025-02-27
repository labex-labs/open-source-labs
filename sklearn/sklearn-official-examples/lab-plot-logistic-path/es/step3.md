# Graficar la trayectoria de regularización

Graficaremos la trayectoria de regularización utilizando los coeficientes de los modelos entrenados. Los coeficientes se graficarán en función del logaritmo de la fuerza de regularización. En el lado izquierdo de la figura (regularizadores fuertes), todos los coeficientes son exactamente 0. A medida que la regularización se vuelve progresivamente menos restrictiva, los coeficientes pueden tomar valores no nulos uno tras otro.

```python
import matplotlib.pyplot as plt

plt.plot(np.log10(cs), coefs_, marker="o")
ymin, ymax = plt.ylim()
plt.xlabel("log(C)")
plt.ylabel("Coefficients")
plt.title("Logistic Regression Path")
plt.axis("tight")
plt.show()
```

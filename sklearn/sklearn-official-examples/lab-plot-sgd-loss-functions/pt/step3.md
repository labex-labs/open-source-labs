# Plotar as Funções de Perda

Plotamos as várias funções de perda convexas suportadas por `scikit-learn` usando a biblioteca `matplotlib`.

```python
lw = 2
plt.plot([xmin, 0, 0, xmax], [1, 1, 0, 0], color="gold", lw=lw, label="Perda zero-um")
plt.plot(xx, np.where(xx < 1, 1 - xx, 0), color="teal", lw=lw, label="Perda Hinge")
plt.plot(xx, -np.minimum(xx, 0), color="yellowgreen", lw=lw, label="Perda Perceptron")
plt.plot(xx, np.log2(1 + np.exp(-xx)), color="cornflowerblue", lw=lw, label="Perda Log")
plt.plot(xx, np.where(xx < 1, 1 - xx, 0) ** 2, color="orange", lw=lw, label="Perda Hinge quadrada")
plt.plot(xx, modified_huber_loss(xx, 1), color="darkorchid", lw=lw, linestyle="--", label="Perda Huber modificada")
plt.ylim((0, 8))
plt.legend(loc="upper right")
plt.xlabel(r"Função de decisão $f(x)$")
plt.ylabel("$L(y=1, f(x))$")
plt.show()
```

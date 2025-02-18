# Graficar el atractor de Lorenz

Graficamos el atractor de Lorenz utilizando el módulo `mplot3d` de Matplotlib.

```python
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")
ax.set_title("Atractor de Lorenz")

plt.show()
```

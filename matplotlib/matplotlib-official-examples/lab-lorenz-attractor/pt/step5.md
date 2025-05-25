# Plotar o Atrator de Lorenz

Plotamos o Atrator de Lorenz usando o módulo mplot3d do Matplotlib.

```python
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("Eixo X")
ax.set_ylabel("Eixo Y")
ax.set_zlabel("Eixo Z")
ax.set_title("Atrator de Lorenz")

plt.show()
```

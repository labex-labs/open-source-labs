# Den Lorenz-Attraktor plotten

Wir plotten den Lorenz-Attraktor mit dem mplot3d-Modul von Matplotlib.

```python
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X-Achse")
ax.set_ylabel("Y-Achse")
ax.set_zlabel("Z-Achse")
ax.set_title("Lorenz-Attraktor")

plt.show()
```

# Построение графика аттрактора Лоренца

Мы строим график аттрактора Лоренца с использованием модуля mplot3d библиотеки Matplotlib.

```python
ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("Ось X")
ax.set_ylabel("Ось Y")
ax.set_zlabel("Ось Z")
ax.set_title("Аттрактор Лоренца")

plt.show()
```

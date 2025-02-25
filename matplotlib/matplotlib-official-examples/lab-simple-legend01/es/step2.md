# Crear una figura y un subdiagrama

Necesitamos crear una figura y un subdiagrama para trazar nuestros datos. Vamos a crear un diagrama con dos subdiagramas.

```python
fig = plt.figure()

ax = fig.add_subplot(211)
ax.plot([1, 2, 3], label="test1")
ax.plot([3, 2, 1], label="test2")

ax = fig.add_subplot(223)
ax.plot([1, 2, 3], label="test1")
ax.plot([3, 2, 1], label="test2")
```

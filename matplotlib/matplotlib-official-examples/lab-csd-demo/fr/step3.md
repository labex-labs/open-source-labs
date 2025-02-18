# Tracer les signaux

Nous pouvons tracer les deux signaux générés en utilisant la fonction `plot` de Matplotlib.

```python
fig, ax = plt.subplots()
ax.plot(t, s1, label='s1')
ax.plot(t, s2, label='s2')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.legend()
plt.show()
```

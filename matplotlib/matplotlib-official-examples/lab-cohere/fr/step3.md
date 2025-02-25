# Tracer les signaux

Nous pouvons maintenant tracer les deux signaux dans le domaine temporel à l'aide de Matplotlib.

```python
fig, axs = plt.subplots(2, 1)
axs[0].plot(t, s1, t, s2)
axs[0].set_xlim(0, 2)
axs[0].set_xlabel('Time')
axs[0].set_ylabel('s1 et s2')
axs[0].grid(True)
```

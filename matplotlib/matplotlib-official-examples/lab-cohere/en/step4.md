# Plot Coherence

We can now plot the coherence of the two signals using Matplotlib's `cohere` function.

```python
cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('Coherence')
```

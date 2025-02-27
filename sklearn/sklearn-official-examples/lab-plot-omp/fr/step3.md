# Tracer le signal sparse

```python
plt.figure(figsize=(7, 7))
plt.subplot(4, 1, 1)
plt.xlim(0, 512)
plt.title("Signal sparse")
plt.stem(idx, w[idx])
```

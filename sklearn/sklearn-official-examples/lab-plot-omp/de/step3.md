# Zeichnen des dünnen Signals

```python
plt.figure(figsize=(7, 7))
plt.subplot(4, 1, 1)
plt.xlim(0, 512)
plt.title("Dünnes Signal")
plt.stem(idx, w[idx])
```

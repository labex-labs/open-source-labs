# Graficar la señal esparsa

```python
plt.figure(figsize=(7, 7))
plt.subplot(4, 1, 1)
plt.xlim(0, 512)
plt.title("Señal esparsa")
plt.stem(idx, w[idx])
```

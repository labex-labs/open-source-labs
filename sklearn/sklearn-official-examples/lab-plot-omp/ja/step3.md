# 疎信号をプロットする

```python
plt.figure(figsize=(7, 7))
plt.subplot(4, 1, 1)
plt.xlim(0, 512)
plt.title("疎信号")
plt.stem(idx, w[idx])
```

# 희소 신호 시각화

```python
plt.figure(figsize=(7, 7))
plt.subplot(4, 1, 1)
plt.xlim(0, 512)
plt.title("희소 신호")
plt.stem(idx, w[idx])
```

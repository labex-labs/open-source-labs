# 이미지 보간 (Interpolate)

```python
# 세 가지 다른 보간 방법을 사용하여 동일한 배열을 보간합니다.
A = np.random.rand(5, 5)

fig, axs = plt.subplots(1, 3, figsize=(10, 3))
for ax, interp in zip(axs, ['nearest', 'bilinear', 'bicubic']):
    ax.imshow(A, interpolation=interp)
    ax.set_title(interp.capitalize())
    ax.grid(True)

plt.show()
```

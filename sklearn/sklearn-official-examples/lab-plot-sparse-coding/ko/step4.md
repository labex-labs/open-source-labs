# 웨이블릿 사전 계산

Matplotlib 을 사용하여 웨이블릿 사전을 계산하고 시각화합니다.

```python
# 웨이블릿 사전 계산
D_fixed = ricker_matrix(width=width, resolution=resolution, n_components=n_components)
D_multi = np.r_[
    tuple(
        ricker_matrix(width=w, resolution=resolution, n_components=n_components // 5)
        for w in (10, 50, 100, 500, 1000)
    )
]

# 웨이블릿 사전 시각화
plt.figure(figsize=(10, 5))
for i, D in enumerate((D_fixed, D_multi)):
    plt.subplot(1, 2, i + 1)
    plt.imshow(D, cmap=plt.cm.gray, interpolation="nearest")
    plt.title("웨이블릿 사전 (%s)" % ("고정 너비" if i == 0 else "여러 너비"))
    plt.axis("off")
plt.show()
```

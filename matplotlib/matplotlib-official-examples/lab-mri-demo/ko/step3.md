# MRI 이미지 표시

`matplotlib`의 `imshow` 함수를 사용하여 MRI 이미지를 흑백으로 표시합니다.

```python
fig, ax = plt.subplots(num="MRI_demo")
ax.imshow(im, cmap="gray")
ax.axis('off')
plt.show()
```

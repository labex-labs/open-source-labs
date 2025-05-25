# 이미지 표시

이제 Matplotlib 의 `imshow` 메서드를 사용하여 이미지를 표시할 수 있습니다. 또한 축을 끄면 이미지 만 볼 수 있습니다.

```python
fig, ax = plt.subplots()
im = ax.imshow(image)
ax.axis('off')
```

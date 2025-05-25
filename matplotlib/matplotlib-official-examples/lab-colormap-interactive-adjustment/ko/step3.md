# 플롯 생성

이제 데이터를 생성했으므로 `imshow()` 함수를 사용하여 플롯을 생성합니다.

```python
fig, ax = plt.subplots()
im = ax.imshow(data2d)
ax.set_title('Pan on the colorbar to shift the color mapping\n'
             'Zoom on the colorbar to scale the color mapping')
```

# 이미지 원점 (Origin) 제어

```python
# 배열 원점 x[0, 0] 을 왼쪽 위 또는 오른쪽 아래로 플롯할지 지정합니다.
x = np.arange(120).reshape((10, 12))

interp = 'bilinear'
fig, axs = plt.subplots(nrows=2, sharex=True, figsize=(3, 5))
axs[0].set_title('파란색이 위로')
axs[0].imshow(x, origin='upper', interpolation=interp)

axs[1].set_title('파란색이 아래로')
axs[1].imshow(x, origin='lower', interpolation=interp)
plt.show()
```

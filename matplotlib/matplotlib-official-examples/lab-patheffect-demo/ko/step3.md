# 등고선에 스트로크 효과 추가

`withStroke` 경로 효과를 사용하여 등고선과 레이블에 스트로크 효과를 추가할 수도 있습니다.

```python
# Create plot and add contour lines with stroke effect
fig, ax = plt.subplots()
ax.imshow(arr)
cntr = ax.contour(arr, colors="k")

plt.setp(cntr.collections, path_effects=[
    patheffects.withStroke(linewidth=3, foreground="w")])

clbls = ax.clabel(cntr, fmt="%2.0f", use_clabeltext=True)
plt.setp(clbls, path_effects=[
    patheffects.withStroke(linewidth=3, foreground="w")])

plt.show()
```

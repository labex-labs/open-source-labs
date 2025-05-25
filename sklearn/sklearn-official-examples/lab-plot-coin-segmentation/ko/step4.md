# 분할 시각화

분할된 영역의 윤곽선을 원본 이미지에 겹쳐서 플롯하여 결과 영역을 시각화합니다.

```python
plt.figure(figsize=(5, 5))
plt.imshow(rescaled_coins, cmap=plt.cm.gray)
plt.xticks(())
plt.yticks(())
title = "스펙트럴 클러스터링: %s, %.2fs" % (assign_labels, (t1 - t0))
print(title)
plt.title(title)
for l in range(n_regions):
    colors = [plt.cm.nipy_spectral((l + 4) / float(n_regions + 4))]
    plt.contour(labels == l, colors=colors)
plt.show()
```

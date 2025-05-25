# 결과 플롯

마지막으로, 이미지에 결과를 플롯할 수 있습니다. Matplotlib 을 사용하여 재조정된 이미지와 클러스터의 윤곽선을 플롯할 것입니다. 각 클러스터를 반복하여 해당 클러스터의 픽셀 윤곽선을 플롯할 것입니다.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(5, 5))
plt.imshow(rescaled_coins, cmap=plt.cm.gray)
for l in range(n_clusters):
    plt.contour(
        label == l,
        colors=[
            plt.cm.nipy_spectral(l / float(n_clusters)),
        ],
    )
plt.axis("off")
plt.show()
```

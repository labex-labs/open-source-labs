# 결과 플롯

`matplotlib.pyplot`의 `matshow`를 사용하여 원본 이미지와 분할된 이미지를 나란히 플롯합니다.

```python
import matplotlib.pyplot as plt

label_im = np.full(mask.shape, -1.0)
label_im[mask] = labels

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axs[0].matshow(img)
axs[1].matshow(label_im)

plt.show()
```

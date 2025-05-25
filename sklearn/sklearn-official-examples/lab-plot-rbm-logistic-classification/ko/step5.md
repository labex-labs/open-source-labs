# 시각화

이 단계에서는 RBM 으로 추출된 100 개의 구성 요소를 시각화합니다. 이미지를 그리기 위해 `matplotlib.pyplot` 모듈을 사용합니다.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(4.2, 4))
for i, comp in enumerate(rbm.components_):
    plt.subplot(10, 10, i + 1)
    plt.imshow(comp.reshape((8, 8)), cmap=plt.cm.gray_r, interpolation="nearest")
    plt.xticks(())
    plt.yticks(())
plt.suptitle("RBM 으로 추출된 100 개의 구성 요소", fontsize=16)
plt.subplots_adjust(0.08, 0.02, 0.92, 0.85, 0.08, 0.23)

plt.show()
```

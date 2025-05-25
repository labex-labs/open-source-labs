# 결과 플롯

원본 숫자와 재샘플링된 숫자를 4x11 그리드에 나란히 플롯합니다.

```python
import matplotlib.pyplot as plt

# 데이터를 4x11 그리드로 변환
new_data = new_data.reshape((4, 11, -1))
real_data = digits.data[:44].reshape((4, 11, -1))

# 실제 숫자와 재샘플링된 숫자 플롯
fig, ax = plt.subplots(9, 11, subplot_kw=dict(xticks=[], yticks=[]))
for j in range(11):
    ax[4, j].set_visible(False)
    for i in range(4):
        im = ax[i, j].imshow(
            real_data[i, j].reshape((8, 8)), cmap=plt.cm.binary, interpolation="nearest"
        )
        im.set_clim(0, 16)
        im = ax[i + 5, j].imshow(
            new_data[i, j].reshape((8, 8)), cmap=plt.cm.binary, interpolation="nearest"
        )
        im.set_clim(0, 16)

ax[0, 5].set_title("입력 데이터에서 선택")
ax[5, 5].set_title("커널 밀도 모델에서 생성된 '새로운' 숫자")

plt.show()
```

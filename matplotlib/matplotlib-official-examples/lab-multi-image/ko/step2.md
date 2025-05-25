# 데이터 생성 및 서브플롯 생성

다음으로, 이미지에 대한 데이터를 생성합니다. 3x2 그리드의 서브플롯을 생성하며, 각 서브플롯은 무작위로 생성된 값의 배열을 포함합니다.

```python
np.random.seed(19680801)
Nr = 3
Nc = 2

fig, axs = plt.subplots(Nr, Nc)
fig.suptitle('Multiple images')

images = []
for i in range(Nr):
    for j in range(Nc):
        # Generate data with a range that varies from one plot to the next.
        data = ((1 + i + j) / 10) * np.random.rand(10, 20)
        images.append(axs[i, j].imshow(data))
        axs[i, j].label_outer()
```

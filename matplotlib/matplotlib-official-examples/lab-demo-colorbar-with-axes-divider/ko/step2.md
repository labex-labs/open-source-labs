# 플롯 생성

다음으로, Matplotlib 의 `imshow` 함수를 사용하여 플롯을 생성합니다. 이 함수는 플롯에 이미지를 표시합니다. 또한 두 개의 서브플롯 (subplot) 이 있는 figure 를 생성합니다.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.subplots_adjust(wspace=0.5)

im1 = ax1.imshow([[1, 2], [3, 4]])

im2 = ax2.imshow([[1, 2], [3, 4]])
```

# 플롯 및 이미지 생성

다음으로, inset axes 를 사용하여 컬러바를 추가하는 방법을 보여주기 위해 플롯과 이미지를 생성합니다.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[6, 3])

im1 = ax1.imshow([[1, 2], [2, 3]])
im2 = ax2.imshow([[1, 2], [2, 3]])
```

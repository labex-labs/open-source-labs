# 원본 이미지 로드 및 표시

먼저 Scipy 에서 족제비 얼굴 이미지를 로드합니다. 이미지를 표시하고 모양, 데이터 유형 및 메모리 사용량을 확인합니다.

```python
from scipy.misc import face
import matplotlib.pyplot as plt

raccoon_face = face(gray=True)

print(f"이미지의 차원은 {raccoon_face.shape}입니다.")
print(f"이미지 인코딩에 사용된 데이터 유형은 {raccoon_face.dtype}입니다.")
print(f"RAM 에서 차지하는 바이트 수는 {raccoon_face.nbytes}입니다.")

fig, ax = plt.subplots(ncols=2, figsize=(12, 4))
ax[0].imshow(raccoon_face, cmap=plt.cm.gray)
ax[0].axis("off")
ax[0].set_title("원본 이미지")
ax[1].hist(raccoon_face.ravel(), bins=256)
ax[1].set_xlabel("픽셀 값")
ax[1].set_ylabel("픽셀 개수")
ax[1].set_title("픽셀 값 분포")
_ = fig.suptitle("족제비 얼굴의 원본 이미지")
```

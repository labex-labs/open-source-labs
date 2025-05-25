# 데이터셋 시각화

데이터셋을 더 잘 이해하기 위해 matplotlib 를 사용하여 샘플 이미지를 시각화할 수 있습니다. 다음 코드는 데이터셋의 마지막 숫자를 표시합니다.

```python
import matplotlib.pyplot as plt

# 마지막 숫자 표시
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
```

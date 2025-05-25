# 특징 순위 시각화

마지막으로, Matplotlib 라이브러리를 사용하여 특징 순위를 시각화합니다. `matshow()` 함수를 사용하여 순위를 이미지로 표시합니다. 또한, 색상 막대와 제목을 플롯에 추가합니다.

```python
import matplotlib.pyplot as plt

plt.matshow(ranking, cmap=plt.cm.Blues)
plt.colorbar()
plt.title("RFE 를 이용한 픽셀 순위")
plt.show()
```

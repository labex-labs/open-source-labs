# 정규화 경로 시각화

학습된 모델의 계수를 사용하여 정규화 경로를 시각화할 것입니다. 계수는 정규화 강도의 로그 값에 대해 플롯될 것입니다. 그림의 왼쪽 (강한 정규화제) 에서는 모든 계수가 정확히 0 입니다. 정규화가 점진적으로 약해짐에 따라 계수가 하나씩 0 이 아닌 값을 가질 수 있습니다.

```python
import matplotlib.pyplot as plt

plt.plot(np.log10(cs), coefs_, marker="o")
ymin, ymax = plt.ylim()
plt.xlabel("log(C)")
plt.ylabel("계수")
plt.title("로지스틱 회귀 경로")
plt.axis("tight")
plt.show()
```

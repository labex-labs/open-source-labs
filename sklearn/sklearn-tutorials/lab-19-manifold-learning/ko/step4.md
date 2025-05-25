# 결과 비교

다양한 다양체 학습 알고리즘의 결과를 비교합니다. 변환된 데이터를 시각화하여 각 알고리즘이 데이터의 기본 구조를 얼마나 잘 보존했는지 확인합니다.

```python
import matplotlib.pyplot as plt

# 변환된 데이터의 산점도를 생성합니다.
plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y)
plt.title('다양체 학습')
plt.xlabel('컴포넌트 1')
plt.ylabel('컴포넌트 2')
plt.show()
```

# 결과 시각화

중첩되지 않은 교차 검증과 중첩 교차 검증의 결과를 막대 그래프로 시각화합니다.

```python
from matplotlib import pyplot as plt

# 차이를 나타내는 막대 그래프를 생성합니다.
plt.bar(["중첩되지 않은", "중첩된"], [non_nested_score, nested_scores.mean()])
plt.ylim([0.9, 1.0])
plt.ylabel("점수")
plt.title("중첩되지 않은 및 중첩 교차 검증 점수")
plt.show()
```

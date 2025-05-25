# 결과 플롯

마지막으로, C 의 함수로서 평균 점수를 플롯하고 표준 편차를 시각화하기 위해 오차 막대도 포함합니다.

```python
import matplotlib.pyplot as plt

plt.figure()
plt.semilogx(C_s, scores)
plt.semilogx(C_s, np.array(scores) + np.array(scores_std), "b--")
plt.semilogx(C_s, np.array(scores) - np.array(scores_std), "b--")
locs, labels = plt.yticks()
plt.yticks(locs, list(map(lambda x: "%g" % x, locs)))
plt.ylabel("CV 점수")
plt.xlabel("매개변수 C")
plt.ylim(0, 1.1)
plt.show()
```

# 결과 플롯

원본 붓꽃 데이터셋과 무작위 데이터 모두에 대한 퍼뮤테이션 점수 (널 분포) 의 히스토그램을 플롯합니다. 또한, 원본 데이터에 대한 분류기의 점수를 빨간색 선으로 표시하고 각 그래프에 p-값을 표시합니다.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# 원본 데이터
ax.hist(perm_scores_iris, bins=20, density=True)
ax.axvline(score_iris, ls="--", color="r")
score_label = f"원본 데이터 점수: {score_iris:.2f}\n(p-값: {pvalue_iris:.3f})"
ax.text(0.7, 10, score_label, fontsize=12)
ax.set_xlabel("정확도 점수")
_ = ax.set_ylabel("확률 밀도")

plt.show()

fig, ax = plt.subplots()

# 무작위 데이터
ax.hist(perm_scores_rand, bins=20, density=True)
ax.set_xlim(0.13)
ax.axvline(score_rand, ls="--", color="r")
score_label = f"원본 데이터 점수: {score_rand:.2f}\n(p-값: {pvalue_rand:.3f})"
ax.text(0.14, 7.5, score_label, fontsize=12)
ax.set_xlabel("정확도 점수")
ax.set_ylabel("확률 밀도")

plt.show()
```

# 결과 비교

다양한 누락 값 보간 전략의 결과를 막대 차트를 통해 비교합니다.

```python
scores = pd.concat(
    [score_full_data, score_simple_imputer, score_iterative_imputer],
    keys=["Original", "SimpleImputer", "IterativeImputer"],
    axis=1,
)

fig, ax = plt.subplots(figsize=(13, 6))
means = -scores.mean()
errors = scores.std()
means.plot.barh(xerr=errors, ax=ax)
ax.set_title("캘리포니아 주택 회귀 분석 - 서로 다른 누락 값 보간 방법 비교")
ax.set_xlabel("MSE (값이 작을수록 좋음)")
ax.set_yticks(np.arange(means.shape[0]))
ax.set_yticklabels([" w/ ".join(label) for label in means.index.tolist()])
plt.tight_layout(pad=1)
plt.show()
```

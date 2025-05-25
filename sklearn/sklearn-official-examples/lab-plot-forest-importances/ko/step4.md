# 불순물 감소 평균 기반 특징 중요도

학습된 속성 `feature_importances_`에서 특징 중요도를 제공하며, 각 트리 내 불순물 감소 누적의 평균 및 표준 편차로 계산됩니다. 불순물 기반 중요도를 플롯합니다.

```python
start_time = time.time()
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
elapsed_time = time.time() - start_time

print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")

forest_importances = pd.Series(importances, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=std, ax=ax)
ax.set_title("Feature importances using MDI")
ax.set_ylabel("Mean decrease in impurity")
fig.tight_layout()
```

# 특성 순열 기반 특징 중요도

순열 특징 중요도는 불순물 기반 특징 중요도의 한계를 극복합니다. 즉, 고카디널리티 특징에 대한 편향이 없으며, 왼쪽으로 제외된 테스트 세트에서 계산할 수 있습니다. 전체 순열 중요도를 계산합니다. 특징은 n 번 셔플되고 모델이 다시 맞춰져서 특징의 중요도를 추정합니다. 중요도 순위를 플롯합니다.

```python
start_time = time.time()
result = permutation_importance(
    forest, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
)
elapsed_time = time.time() - start_time
print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")

forest_importances = pd.Series(result.importances_mean, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=result.importances_std, ax=ax)
ax.set_title("Feature importances using permutation on full model")
ax.set_ylabel("Mean accuracy decrease")
fig.tight_layout()
plt.show()
```

# 결과 분석

검색 객체의 `cv_results_` 속성에는 검색 결과가 포함되어 있습니다. 다음 코드를 사용하여 pandas 데이터프레임으로 변환합니다.

```python
results = pd.DataFrame(rsh.cv_results_)
```

`params` 열을 문자열로 변환하여 `params_str` 열을 생성합니다. 동일한 `params_str` 및 `iter` 값을 가진 중복 행을 제거합니다.

```python
results["params_str"] = results.params.apply(str)
results.drop_duplicates(subset=("params_str", "iter"), inplace=True)
```

이후 `pivot` 메서드를 사용하여 반복 횟수와 매개변수 조합에 대한 평균 테스트 점수를 피벗합니다.

```python
mean_scores = results.pivot(
    index="iter", columns="params_str", values="mean_test_score"
)
```

마지막으로, 다음 코드를 사용하여 반복에 따른 평균 테스트 점수를 플롯합니다.

```python
ax = mean_scores.plot(legend=False, alpha=0.6)

labels = [
    f"iter={i}\nn_samples={rsh.n_resources_[i]}\nn_candidates={rsh.n_candidates_[i]}"
    for i in range(rsh.n_iterations_)
]

ax.set_xticks(range(rsh.n_iterations_))
ax.set_xticklabels(labels, rotation=45, multialignment="left")
ax.set_title("반복에 따른 후보자 점수")
ax.set_ylabel("평균 테스트 점수", fontsize=15)
ax.set_xlabel("반복 횟수", fontsize=15)
plt.tight_layout()
plt.show()
```

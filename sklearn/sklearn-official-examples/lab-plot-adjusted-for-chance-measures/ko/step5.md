# 실험 2 결과 시각화

`matplotlib` 라이브러리를 사용하여 두 번째 실험 결과를 시각화합니다. 첫 번째 실험과 유사한 결과를 관찰합니다. 기회에 대한 조정된 지표는 0 에 가깝게 유지되는 반면, 다른 지표는 레이블링이 더 세분화됨에 따라 증가하는 경향이 있습니다. 측정에 사용된 총 샘플 수에 클러스터 수가 가까워질수록 랜덤 레이블링의 평균 V-측정값이 상당히 증가합니다.

```python
n_samples = 100
n_clusters_range = np.linspace(2, n_samples, 10).astype(int)

plt.figure(2)

plots = []
names = []

for marker, (score_name, score_func) in zip("d^vx.,", score_funcs):
    scores = uniform_labelings_scores(score_func, n_samples, n_clusters_range)
    plots.append(
        plt.errorbar(
            n_clusters_range,
            np.median(scores, axis=1),
            scores.std(axis=1),
            alpha=0.8,
            linewidth=2,
            marker=marker,
        )[0]
    )
    names.append(score_name)

plt.title(
    "2 개의 랜덤 균일 레이블링에 대한 클러스터링 측정값\n클러스터 수가 동일한 경우"
)
plt.xlabel(f"클러스터 수 (샘플 수는 {n_samples}로 고정)")
plt.ylabel("점수 값")
plt.legend(plots, names)
plt.ylim(bottom=-0.05, top=1.05)
plt.show()
```

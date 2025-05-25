# 실험 1 결과 시각화

`matplotlib` 및 `seaborn` 라이브러리를 사용하여 첫 번째 실험 결과를 시각화합니다. 랜드 지수는 `n_clusters`가 `n_classes`보다 클 경우 포화됩니다. V-측도와 같은 다른 조정되지 않은 측정값은 클러스터 수와 샘플 수 사이에 선형적인 의존성을 보여줍니다. 기회에 대한 조정 측정값 (예: ARI 및 AMI) 은 샘플 수와 클러스터 수에 관계없이 평균 점수 0.0 주변에 중심을 둔 일부 랜덤 변동을 보입니다.

```python
import matplotlib.pyplot as plt
import seaborn as sns

n_samples = 1000
n_classes = 10
n_clusters_range = np.linspace(2, 100, 10).astype(int)
plots = []
names = []

sns.color_palette("colorblind")
plt.figure(1)

for marker, (score_name, score_func) in zip("d^vx.,", score_funcs):
    scores = fixed_classes_uniform_labelings_scores(
        score_func, n_samples, n_clusters_range, n_classes=n_classes
    )
    plots.append(
        plt.errorbar(
            n_clusters_range,
            scores.mean(axis=1),
            scores.std(axis=1),
            alpha=0.8,
            linewidth=1,
            marker=marker,
        )[0]
    )
    names.append(score_name)

plt.title(
    "랜덤 균일 레이블링에 대한 클러스터링 측정값\n"
    f"{n_classes}개 클래스를 가진 참조 할당과 비교"
)
plt.xlabel(f"클러스터 수 (샘플 수는 {n_samples}로 고정)")
plt.ylabel("점수 값")
plt.ylim(bottom=-0.05, top=1.05)
plt.legend(plots, names, bbox_to_anchor=(0.5, 0.5))
plt.show()
```

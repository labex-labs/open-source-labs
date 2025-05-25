# Varimax 회전을 사용한 요인 분석 실행

이제 아이리스 데이터셋에 Varimax 회전을 적용한 요인 분석을 수행하여 데이터의 기저 구조를 파악해 보겠습니다. PCA 와 비회전 요인 분석 결과와 비교해 보겠습니다.

```python
# Varimax 회전을 사용한 요인 분석 실행
n_comps = 2

methods = [
    ("PCA", PCA()),
    ("비회전 요인 분석", FactorAnalysis()),
    ("Varimax 요인 분석", FactorAnalysis(rotation="varimax")),
]
fig, axes = plt.subplots(ncols=len(methods), figsize=(10, 8), sharey=True)

for ax, (method, fa) in zip(axes, methods):
    fa.set_params(n_components=n_comps)
    fa.fit(X)

    components = fa.components_.T
    print("\n\n %s :\n" % method)
    print(components)

    vmax = np.abs(components).max()
    ax.imshow(components, cmap="RdBu_r", vmax=vmax, vmin=-vmax)
    ax.set_yticks(np.arange(len(feature_names)))
    ax.set_yticklabels(feature_names)
    ax.set_title(str(method))
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Comp. 1", "Comp. 2"])
fig.suptitle("요인들")
plt.tight_layout()
plt.show()
```

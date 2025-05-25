# 결과 비교

다양한 방법의 결과를 학습 시간과 함께 플롯하여 성능을 비교합니다.

```python
import matplotlib.pyplot as plt

# 다양한 방법의 결과 플롯
fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(
    [
        lsvm_time,
    ],
    [
        lsvm_score,
    ],
    label="선형 SVM",
    c="green",
    marker="^",
)

for n_components in N_COMPONENTS:
    ax.scatter(
        [
            results[f"LSVM + PS({n_components})"]["time"],
        ],
        [
            results[f"LSVM + PS({n_components})"]["score"],
        ],
        c="blue",
    )
    ax.annotate(
        f"n_comp.={n_components}",
        (
            results[f"LSVM + PS({n_components})"]["time"],
            results[f"LSVM + PS({n_components})"]["score"],
        ),
        xytext=(-30, 10),
        textcoords="offset pixels",
    )

ax.scatter(
    [
        ksvm_time,
    ],
    [
        ksvm_score,
    ],
    label="커널 SVM",
    c="red",
    marker="x",
)

ax.set_xlabel("학습 시간 (초)")
ax.set_ylabel("정확도 (%)")
ax.legend()
plt.show()
```

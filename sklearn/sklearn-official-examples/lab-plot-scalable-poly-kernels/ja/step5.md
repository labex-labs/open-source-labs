# 結果を比較する

異なる手法の結果を訓練時間に対してプロットし、それらの性能を比較します。

```python
import matplotlib.pyplot as plt

# 異なる手法の結果をプロット
fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(
    [
        lsvm_time,
    ],
    [
        lsvm_score,
    ],
    label="Linear SVM",
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
    label="Kernel SVM",
    c="red",
    marker="x",
)

ax.set_xlabel("Training time (s)")
ax.set_ylabel("Accuracy (%)")
ax.legend()
plt.show()
```

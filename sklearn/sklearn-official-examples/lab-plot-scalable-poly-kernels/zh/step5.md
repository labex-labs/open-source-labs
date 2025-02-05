# 比较结果

我们将绘制不同方法的结果与它们的训练时间，以比较它们的性能。

```python
import matplotlib.pyplot as plt

# 绘制不同方法的结果
fig, ax = plt.subplots(figsize=(7, 7))
ax.scatter(
    [
        lsvm_time,
    ],
    [
        lsvm_score,
    ],
    label="线性支持向量机",
    c="绿色",
    marker="^",
)

for n_components in N_COMPONENTS:
    ax.scatter(
        [
            results[f"线性支持向量机 + PS({n_components})"]["时间"],
        ],
        [
            results[f"线性支持向量机 + PS({n_components})"]["得分"],
        ],
        c="蓝色",
    )
    ax.annotate(
        f"组件数量={n_components}",
        (
            results[f"线性支持向量机 + PS({n_components})"]["时间"],
            results[f"线性支持向量机 + PS({n_components})"]["得分"],
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
    label="核支持向量机",
    c="红色",
    marker="x",
)

ax.set_xlabel("训练时间（秒）")
ax.set_ylabel("准确率（%）")
ax.legend()
plt.show()
```

需注意，代码中的`results`变量在前面未定义，可能会导致运行时错误，实际使用时请确保其已正确定义。

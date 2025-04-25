# 绘制结果

```python
# 绘制准确率变化
plt.figure()
for _, stats in sorted(cls_stats.items()):
    # 绘制准确率随示例数量的变化
    accuracy, n_examples = zip(*stats["accuracy_history"])
    plot_accuracy(n_examples, accuracy, "训练示例数量 (#)")
    ax = plt.gca()
    ax.set_ylim((0.8, 1))
plt.legend(cls_names, loc="最佳")

plt.figure()
for _, stats in sorted(cls_stats.items()):
    # 绘制准确率随运行时间的变化
    accuracy, runtime = zip(*stats["runtime_history"])
    plot_accuracy(runtime, accuracy, "运行时间 (秒)")
    ax = plt.gca()
    ax.set_ylim((0.8, 1))
plt.legend(cls_names, loc="最佳")

# 绘制拟合时间
plt.figure()
fig = plt.gcf()
cls_runtime = [stats["total_fit_time"] for cls_name, stats in sorted(cls_stats.items())]

cls_runtime.append(total_vect_time)
cls_names.append("向量化")
bar_colors = ["b", "g", "r", "c", "m", "y"]

ax = plt.subplot(111)
rectangles = plt.bar(range(len(cls_names)), cls_runtime, width=0.5, color=bar_colors)

ax.set_xticks(np.linspace(0, len(cls_names) - 1, len(cls_names)))
ax.set_xticklabels(cls_names, fontsize=10)
ymax = max(cls_runtime) * 1.2
ax.set_ylim((0, ymax))
ax.set_ylabel("运行时间 (秒)")
ax.set_title("训练时间")


def autolabel(rectangles):
    """在矩形上附加一些文本作为自动标签。"""
    for rect in rectangles:
        height = rect.get_height()
        ax.text(
            rect.get_x() + rect.get_width() / 2.0,
            1.05 * height,
            "%.4f" % height,
            ha="中心",
            va="底部",
        )
        plt.setp(plt.xticks()[1], rotation=30)


autolabel(rectangles)
plt.tight_layout()
plt.show()

# 绘制预测时间
plt.figure()
cls_runtime = []
cls_names = list(sorted(cls_stats.keys()))
for cls_name, stats in sorted(cls_stats.items()):
    cls_runtime.append(stats["prediction_time"])
cls_runtime.append(parsing_time)
cls_names.append("读取/解析\n+ 特征提取")
cls_runtime.append(vectorizing_time)
cls_names.append("哈希\n+ 向量化")

ax = plt.subplot(111)
rectangles = plt.bar(range(len(cls_names)), cls_runtime, width=0.5, color=bar_colors)

ax.set_xticks(np.linspace(0, len(cls_names) - 1, len(cls_names)))
ax.set_xticklabels(cls_names, fontsize=8)
plt.setp(plt.xticks()[1], rotation=30)
ymax = max(cls_runtime) * 1.2
ax.set_ylim((0, ymax))
ax.set_ylabel("运行时间 (秒)")
ax.set_title("预测时间 (%d 个实例)" % n_test_documents)
autolabel(rectangles)
plt.tight_layout()
plt.show()
```

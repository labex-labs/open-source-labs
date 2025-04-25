# 生成网格并绘图

我们在二维单纯形上生成一组可能的未校准概率网格，计算相应的校准概率，并为每个概率绘制箭头。箭头根据最高的未校准概率进行着色。这展示了学习到的校准映射：

```python
plt.figure(figsize=(10, 10))
# 生成概率值网格
p1d = np.linspace(0, 1, 20)
p0, p1 = np.meshgrid(p1d, p1d)
p2 = 1 - p0 - p1
p = np.c_[p0.ravel(), p1.ravel(), p2.ravel()]
p = p[p[:, 2] >= 0]

# 使用三个类别校准器计算校准概率
calibrated_classifier = cal_clf.calibrated_classifiers_[0]
prediction = np.vstack(
    [
        calibrator.predict(this_p)
        for calibrator, this_p in zip(calibrated_classifier.calibrators, p.T)
    ]
).T

# 重新归一化校准后的预测结果，以确保它们保持在单纯形内。在多类别问题上，CalibratedClassifierCV 的 predict 方法内部也会执行相同的归一化步骤。
prediction /= prediction.sum(axis=1)[:, None]

# 绘制校准器引起的预测概率变化
for i in range(prediction.shape[0]):
    plt.arrow(
        p[i, 0],
        p[i, 1],
        prediction[i, 0] - p[i, 0],
        prediction[i, 1] - p[i, 1],
        head_width=1e-2,
        color=colors[np.argmax(p[i])],
    )

# 绘制单位单纯形的边界
plt.plot([0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], "k", label="单纯形")

plt.grid(False)
for x in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    plt.plot([0, x], [x, 0], "k", alpha=0.2)
    plt.plot([0, 0 + (1 - x) / 2], [x, x + (1 - x) / 2], "k", alpha=0.2)
    plt.plot([x, x + (1 - x) / 2], [0, 0 + (1 - x) / 2], "k", alpha=0.2)

plt.title("学习到的 sigmoid 校准映射")
plt.xlabel("类别 1 的概率")
plt.ylabel("类别 2 的概率")
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)

plt.show()
```

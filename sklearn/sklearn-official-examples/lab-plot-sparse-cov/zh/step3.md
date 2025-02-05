# 绘制结果

第三步是绘制结果。我们绘制协方差矩阵和精度矩阵，还绘制模型选择指标。

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.subplots_adjust(left=0.02, right=0.98)

# 绘制协方差矩阵
covs = [
    ("经验协方差", emp_cov),
    ("莱杜瓦 - 沃尔夫协方差", lw_cov_),
    ("图形拉索交叉验证协方差", cov_),
    ("真实协方差", cov),
]
vmax = cov_.max()
for i, (name, this_cov) in enumerate(covs):
    plt.subplot(2, 4, i + 1)
    plt.imshow(
        this_cov, interpolation="nearest", vmin=-vmax, vmax=vmax, cmap=plt.cm.RdBu_r
    )
    plt.xticks(())
    plt.yticks(())
    plt.title("%s协方差" % name)


# 绘制精度矩阵
precs = [
    ("经验精度", linalg.inv(emp_cov)),
    ("莱杜瓦 - 沃尔夫精度", lw_prec_),
    ("图形拉索精度", prec_),
    ("真实精度", prec),
]
vmax = 0.9 * prec_.max()
for i, (name, this_prec) in enumerate(precs):
    ax = plt.subplot(2, 4, i + 5)
    plt.imshow(
        np.ma.masked_equal(this_prec, 0),
        interpolation="nearest",
        vmin=-vmax,
        vmax=vmax,
        cmap=plt.cm.RdBu_r,
    )
    plt.xticks(())
    plt.yticks(())
    plt.title("%s精度" % name)
    if hasattr(ax, "set_facecolor"):
        ax.set_facecolor(".7")
    else:
        ax.set_axis_bgcolor(".7")

# 绘制模型选择指标
plt.figure(figsize=(4, 3))
plt.axes([0.2, 0.15, 0.75, 0.7])
plt.plot(model.cv_results_["alphas"], model.cv_results_["mean_test_score"], "o-")
plt.axvline(model.alpha_, color=".5")
plt.title("模型选择")
plt.ylabel("交叉验证分数")
plt.xlabel("alpha")

plt.show()
```

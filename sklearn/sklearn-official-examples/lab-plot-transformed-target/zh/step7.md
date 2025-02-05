# 绘制艾姆斯房屋数据的目标分布

我们绘制应用分位数变换器（QuantileTransformer）前后目标的概率密度函数。

```python
f, (ax0, ax1) = plt.subplots(1, 2)

ax0.hist(y, bins=100, density=True)
ax0.set_ylabel("概率")
ax0.set_xlabel("目标")
ax0.set_title("目标分布")

ax1.hist(y_trans, bins=100, density=True)
ax1.set_ylabel("概率")
ax1.set_xlabel("目标")
ax1.set_title("变换后的目标分布")

f.suptitle("艾姆斯房屋数据：售价", y=1.05)
plt.tight_layout()
```

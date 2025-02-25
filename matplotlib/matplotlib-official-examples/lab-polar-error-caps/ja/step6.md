# 重なり合うtheta誤差棒を作成する

このステップでは、出力プロットの読みやすさを低下させる方法を示すために、重なり合うtheta誤差棒を作成します。

```python
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection='polar')
ax.errorbar(theta, r, xerr=5.25, yerr=0.1, capsize=7, fmt="o", c="darkred")
ax.set_title("Overlapping Theta Error Bars")
plt.show()
```

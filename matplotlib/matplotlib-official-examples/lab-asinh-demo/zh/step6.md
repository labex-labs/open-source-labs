# 比较二维柯西分布随机数上的 “symlog” 和 “asinh” 缩放

最后，我们将比较二维柯西分布随机数上的 “symlog” 和 “asinh” 缩放。我们将把同一个图绘制两次，一次使用 “symlog”，另一次使用 “asinh”。

```python
fig3 = plt.figure()
ax = fig3.subplots(1, 1)
r = 3 * np.tan(np.random.uniform(-np.pi / 2.02, np.pi / 2.02,
                                 size=(5000,)))
th = np.random.uniform(0, 2*np.pi, size=r.shape)

ax.scatter(r * np.cos(th), r * np.sin(th), s=4, alpha=0.5)
ax.set_xscale('asinh')
ax.set_yscale('symlog')
ax.set_xlabel('asinh')
ax.set_ylabel('symlog')
ax.set_title('2D Cauchy random deviates')
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.grid()
```

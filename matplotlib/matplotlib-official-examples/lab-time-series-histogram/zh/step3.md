# 使用折线图可视化数据

在这一步中，我们将使用折线图来可视化生成的数据。

```python
# Plot series using `plot` and a small value of `alpha`.
# With this view, it is very difficult to observe the sinusoidal behavior because of how many overlapping series there are.
# It also takes a bit of time to run because so many individual artists need to be generated.
tic = time.time()
plt.plot(x, Y.T, color="C0", alpha=0.1)
toc = time.time()
plt.title("Line plot with alpha")
plt.show()
print(f"{toc-tic:.3f} sec. elapsed")
```

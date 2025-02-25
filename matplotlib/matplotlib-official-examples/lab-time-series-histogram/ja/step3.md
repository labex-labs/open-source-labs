# 折れ線グラフでデータを可視化する

このステップでは、生成したデータを折れ線グラフで可視化します。

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

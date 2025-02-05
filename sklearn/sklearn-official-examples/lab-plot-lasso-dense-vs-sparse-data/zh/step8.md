# 将Lasso应用于稀疏数据

我们使用Scikit-learn的`fit`函数将Lasso回归模型应用于稀疏数据。我们还对拟合过程进行计时，并打印每个Lasso模型的时间。

```python
t0 = time()
sparse_lasso.fit(Xs_sp, y)
print(f"Sparse Lasso done in {(time() - t0):.3f}s")

t0 = time()
dense_lasso.fit(Xs, y)
print(f"Dense Lasso done in  {(time() - t0):.3f}s")
```

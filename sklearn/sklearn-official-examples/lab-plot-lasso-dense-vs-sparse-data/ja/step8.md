# 疎データにLassoを適合させる

Scikit-learnの`fit`関数を使って、Lasso回帰モデルを疎データに適合させます。また、適合プロセスに時間を計測し、各Lassoモデルの時間を表示します。

```python
t0 = time()
sparse_lasso.fit(Xs_sp, y)
print(f"Sparse Lasso done in {(time() - t0):.3f}s")

t0 = time()
dense_lasso.fit(Xs, y)
print(f"Dense Lasso done in  {(time() - t0):.3f}s")
```

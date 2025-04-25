# 疎データに Lasso を適合させる

Scikit-learn の`fit`関数を使って、Lasso 回帰モデルを疎データに適合させます。また、適合プロセスに時間を計測し、各 Lasso モデルの時間を表示します。

```python
t0 = time()
sparse_lasso.fit(Xs_sp, y)
print(f"Sparse Lasso done in {(time() - t0):.3f}s")

t0 = time()
dense_lasso.fit(Xs, y)
print(f"Dense Lasso done in  {(time() - t0):.3f}s")
```

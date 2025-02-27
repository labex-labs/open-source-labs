# 交差検定により非ゼロ数を設定したノイジーな再構成をプロットする

```python
omp_cv = OrthogonalMatchingPursuitCV()
omp_cv.fit(X, y_noisy)
coef = omp_cv.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 4)
plt.xlim(0, 512)
plt.title("交差検定を用いたノイジーな測定値から回復した信号")
plt.stem(idx_r, coef[idx_r])

plt.subplots_adjust(0.06, 0.04, 0.94, 0.90, 0.20, 0.38)
plt.suptitle("直交マッチング追跡による疎信号回復", fontsize=16)
plt.show()
```

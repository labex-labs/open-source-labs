# 교차검증 (CV) 를 이용한 노이즈가 있는 재구성 시각화

```python
omp_cv = OrthogonalMatchingPursuitCV()
omp_cv.fit(X, y_noisy)
coef = omp_cv.coef_
(idx_r,) = coef.nonzero()
plt.subplot(4, 1, 4)
plt.xlim(0, 512)
plt.title("CV 를 이용한 노이즈가 있는 측정값으로부터 복원된 신호")
plt.stem(idx_r, coef[idx_r])

plt.subplots_adjust(0.06, 0.04, 0.94, 0.90, 0.20, 0.38)
plt.suptitle("직교 매칭 추구 (OMP) 를 이용한 희소 신호 복원", fontsize=16)
plt.show()
```

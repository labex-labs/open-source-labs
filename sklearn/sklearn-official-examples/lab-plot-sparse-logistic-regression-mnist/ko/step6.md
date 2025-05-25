# 모델 시각화

각 클래스에 대한 분류 벡터를 플롯하여 모델을 시각화합니다.

```python
coef = clf.coef_.copy()
plt.figure(figsize=(10, 5))
scale = np.abs(coef).max()
for i in range(10):
    l1_plot = plt.subplot(2, 5, i + 1)
    l1_plot.imshow(
        coef[i].reshape(28, 28),
        interpolation="nearest",
        cmap=plt.cm.RdBu,
        vmin=-scale,
        vmax=scale,
    )
    l1_plot.set_xticks(())
    l1_plot.set_yticks(())
    l1_plot.set_xlabel("클래스 %i" % i)
plt.suptitle("분류 벡터...")

run_time = time.time() - t0
print("예제 실행 시간 %.3f 초" % run_time)
plt.show()
```

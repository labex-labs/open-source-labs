# 데이터셋 플롯

이제 `plot_2d` 함수를 사용하여 랜덤으로 생성된 다중 레이블 데이터셋을 플롯합니다. 두 개의 서브플롯이 있는 그림을 만들고, 다른 매개변수 값으로 각 서브플롯에 `plot_2d` 함수를 호출합니다.

```python
_, (ax1, ax2) = plt.subplots(1, 2, sharex="row", sharey="row", figsize=(8, 4))
plt.subplots_adjust(bottom=0.15)

p_c, p_w_c = plot_2d(ax1, n_labels=1)
ax1.set_title("n_labels=1, length=50")
ax1.set_ylabel("Feature 1 count")

plot_2d(ax2, n_labels=3)
ax2.set_title("n_labels=3, length=50")
ax2.set_xlim(left=0, auto=True)
ax2.set_ylim(bottom=0, auto=True)

plt.show()
```

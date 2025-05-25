# 플롯 생성

이 단계에서는 `plot_beta_hist()` 함수를 호출하고 매개변수를 전달하여 플롯을 생성합니다.

```python
fig, ax = plt.subplots()
plot_beta_hist(ax, 10, 10)
plot_beta_hist(ax, 4, 12)
plot_beta_hist(ax, 50, 12)
plot_beta_hist(ax, 6, 55)
ax.set_title("'bmh' style sheet")

plt.show()
```

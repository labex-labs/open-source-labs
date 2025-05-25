# 막대 컨테이너 및 애니메이션 생성

`plt.hist`를 사용하면 `Rectangle` 인스턴스의 모음인 `BarContainer`의 인스턴스를 얻을 수 있습니다. `FuncAnimation`을 사용하여 애니메이션을 설정합니다.

```python
# Using plt.hist allows us to get an instance of BarContainer, which is a
# collection of Rectangle instances. Calling prepare_animation will define
# animate function working with supplied BarContainer, all this is used to setup FuncAnimation.
fig, ax = plt.subplots()
_, _, bar_container = ax.hist(data, HIST_BINS, lw=1, ec="yellow", fc="green", alpha=0.5)
ax.set_ylim(top=55)  # set safe limit to ensure that all data is visible.

ani = animation.FuncAnimation(fig, animate, 50, repeat=False, blit=True)
plt.show()
```

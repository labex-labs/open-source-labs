# Создайте контейнер для столбцов и анимацию

Использование `plt.hist` позволяет получить экземпляр `BarContainer`, который представляет собой коллекцию экземпляров `Rectangle`. Мы используем `FuncAnimation` для настройки анимации.

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

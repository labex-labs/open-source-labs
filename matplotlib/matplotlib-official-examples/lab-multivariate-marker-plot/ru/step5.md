# Создание графика

В этом шаге вы создадите график, используя ранее сгенерированные случайные данные. В частности, вы будете отображать каждую точку данных в виде маркера с символом успеха, определенным переменной успеха, размером, определенным переменной навыка, поворотом, определенным переменной углом взлета, и цветом, определенным переменной тяги.

```python
fig, ax = plt.subplots()
fig.suptitle("Throwing success", size=14)
for skill, takeoff, thrust, mood, pos in data:
    t = Affine2D().scale(skill).rotate_deg(takeoff)
    m = MarkerStyle(SUCCESS_SYMBOLS[mood], transform=t)
    ax.plot(pos[0], pos[1], marker=m, color=cmap(thrust))
fig.colorbar(plt.cm.ScalarMappable(norm=Normalize(0, 1), cmap=cmap),
             ax=ax, label="Normalized Thrust [a.u.]")
ax.set_xlabel("X position [m]")
ax.set_ylabel("Y position [m]")
```

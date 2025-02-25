# Создаем контурные подписи с пользовательскими форматтерами уровней

Теперь мы создадим контурные подписи с пользовательскими форматтерами уровней. Это позволит нам форматировать подписи определенным образом. В этом случае мы удалим конечные нули и добавим знак процента.

```python
def fmt(x):
    s = f"{x:.1f}"
    if s.endswith("0"):
        s = f"{x:.0f}"
    return rf"{s} \%" if plt.rcParams["text.usetex"] else f"{s} %"

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=10)
```

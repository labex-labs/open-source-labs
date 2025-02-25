# Создаем первый событийный график - горизонтальное расположение

Мы создадим первый событийный график в горизонтальном расположении.

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1)
```

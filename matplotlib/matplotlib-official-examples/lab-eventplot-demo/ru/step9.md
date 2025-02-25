# Создаем второй событийный график - вертикальное расположение

Мы создадим второй событийный график в вертикальном расположении.

```python
axs[1, 1].eventplot(data2, colors=colors2, lineoffsets=lineoffsets2,
                    linelengths=linelengths2, orientation='vertical')
```

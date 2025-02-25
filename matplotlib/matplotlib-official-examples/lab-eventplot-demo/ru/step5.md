# Создаем первый событийный график - вертикальное расположение

Мы создадим первый событийный график в вертикальном расположении.

```python
axs[1, 0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1, orientation='vertical')
```

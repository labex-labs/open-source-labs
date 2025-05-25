# 첫 번째 이벤트 플롯 생성 - 수평 방향

첫 번째 이벤트 플롯을 수평 방향으로 생성합니다.

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1)
```

# 플롯 생성

이제 `matplotlib.pyplot`을 사용하여 플롯을 생성합니다. 사인파를 플롯하고 y=0 위치에 수평선을 추가합니다.

```python
fig, ax = plt.subplots()

ax.plot(t, s, color='black')
ax.axhline(0, color='black')
```

# 플롯 생성

이제 `matplotlib.pyplot` 라이브러리를 사용하여 플롯을 생성합니다. 플롯의 x 및 y 제한을 설정한 다음 데이터를 플롯합니다.

```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
```

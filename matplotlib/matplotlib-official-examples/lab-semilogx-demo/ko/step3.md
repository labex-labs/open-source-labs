# 플롯 생성 및 x 축을 로그 스케일로 설정

`subplots()` 메서드를 사용하여 figure 및 axes 객체를 생성합니다. 그런 다음 `semilogx()` 메서드를 사용하여 지수 감쇠 함수를 플롯하고, `set_xscale()` 메서드를 사용하여 x 축을 로그 스케일로 설정합니다. 또한 `grid()` 메서드를 사용하여 플롯에 그리드를 추가합니다.

```python
fig, ax = plt.subplots()

ax.semilogx(t, np.exp(-t / 5.0))
ax.set_xscale('log')
ax.grid()
```

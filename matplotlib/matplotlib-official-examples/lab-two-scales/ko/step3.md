# 플롯 생성

이제 데이터를 갖추었으니 플롯을 생성할 수 있습니다. `matplotlib.pyplot.subplots()`를 사용하여 axes 객체를 생성하는 것으로 시작합니다. 그런 다음 이 axes 객체에 첫 번째 데이터 세트를 플롯하고 레이블 색상을 빨간색으로 설정합니다.

```python
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)
```

다음으로, `ax1.twinx()` 메서드를 사용하여 첫 번째 axes 객체와 동일한 x 축을 공유하는 두 번째 axes 객체를 인스턴스화합니다. 그런 다음 이 새로운 axes 객체에 두 번째 데이터 세트를 플롯하고 레이블 색상을 파란색으로 설정합니다.

```python
ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)
```

마지막으로, `fig.tight_layout()` 메서드를 사용하여 플롯의 레이아웃을 조정하고 `matplotlib.pyplot.show()`를 사용하여 표시합니다.

```python
fig.tight_layout()
plt.show()
```

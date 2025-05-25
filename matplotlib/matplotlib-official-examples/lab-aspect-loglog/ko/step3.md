# 조절 가능한 데이터림 (datalim) 을 가진 로그 - 로그 플롯 생성

다음으로, 조절 가능한 데이터림 (datalim) 을 가진 로그 - 로그 플롯을 생성합니다. 이는 x 축과 y 축 모두 로그 스케일을 가지며, 플롯의 종횡비가 데이터에 맞게 조정된다는 것을 의미합니다.

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_adjustable("datalim")
ax.plot([1, 3, 10], [1, 9, 100], "o-")
ax.set_xlim(1e-1, 1e2)
ax.set_ylim(1e-1, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Datalim")
plt.show()
```

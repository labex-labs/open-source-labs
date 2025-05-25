# 조절 가능한 박스를 가진 로그 - 로그 플롯 생성

다음으로, 조절 가능한 박스를 가진 로그 - 로그 플롯을 생성합니다. 이는 x 축과 y 축 모두 로그 스케일을 가지며, 플롯의 종횡비가 1 과 같다는 것을 의미합니다.

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e1, 1e3)
ax.set_ylim(1e2, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Box")
plt.show()
```

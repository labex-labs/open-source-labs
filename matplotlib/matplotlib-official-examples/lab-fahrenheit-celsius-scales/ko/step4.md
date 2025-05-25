# 플롯 생성

이제 `matplotlib.pyplot`의 `subplots()` 함수를 사용하여 두 개의 y 축이 있는 플롯을 생성합니다. 또한 첫 번째 축의 `ylim_changed` 이벤트를 `convert_ax_c_to_celsius()` 함수에 연결합니다.

```python
fig, ax_f = plt.subplots()
ax_c = ax_f.twinx()

ax_f.callbacks.connect("ylim_changed", convert_ax_c_to_celsius)
```

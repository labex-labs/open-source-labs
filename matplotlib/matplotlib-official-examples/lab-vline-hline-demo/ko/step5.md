# 수직선 추가

이 단계에서는 플롯에 수직선을 추가합니다. Matplotlib 의 `vlines` 함수를 사용하여 수직선을 그립니다. 또한 `transform` 매개변수를 사용하여 y 좌표가 0 에서 1 로 스케일링되도록 설정합니다. x=1 과 x=2 에서 두 개의 수직선을 그립니다.

```python
# Add vertical lines
vax.plot(t, s + nse, '^')
vax.vlines(t, [0], s)
vax.vlines([1, 2], 0, 1, transform=vax.get_xaxis_transform(), colors='r')
vax.set_xlabel('time (s)')
vax.set_title('Vertical lines demo')
```

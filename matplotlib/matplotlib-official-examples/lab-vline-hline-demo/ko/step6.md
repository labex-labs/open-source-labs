# 수평선 추가

이 단계에서는 플롯에 수평선을 추가합니다. Matplotlib 의 `hlines` 함수를 사용하여 수평선을 그립니다. y=0.5, y=2.5, y=4.5 에서 수평선을 그립니다.

```python
# Add horizontal lines
hax.plot(s + nse, t, '^')
hax.hlines(t, [0], s, lw=2)
hax.set_xlabel('time (s)')
hax.set_title('Horizontal lines demo')
```

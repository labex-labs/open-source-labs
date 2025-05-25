# 데이터 플롯팅

2 단계에서 생성된 랜덤 데이터를 `plot()` 함수를 사용하여 두 번 플롯합니다. 첫 번째 플롯은 alpha 값이 0.2 이고, 두 번째 플롯은 alpha 값이 1.0 이며, 클립 경로 (clip path) 가 노란색 원 패치로 설정됩니다.

```python
ax.plot(x, y, alpha=0.2)
line, = ax.plot(x, y, alpha=1.0, clip_path=circ)
ax.set_title("Left click and drag to move looking glass")
```

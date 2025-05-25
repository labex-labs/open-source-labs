# 희소 패턴 플로팅

`spy` 함수를 사용하여 배열의 희소 패턴을 플로팅합니다. 플롯을 사용자 정의하기 위해 `markersize` 및 `precision`과 같은 다양한 매개변수를 사용합니다.

```python
ax1.spy(x, markersize=5)
ax2.spy(x, precision=0.1, markersize=5)
ax3.spy(x)
ax4.spy(x, precision=0.1)
```

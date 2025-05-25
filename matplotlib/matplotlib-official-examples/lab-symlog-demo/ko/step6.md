# x 축과 y 축 모두에 Symlog 플롯 생성

세 번째 서브플롯에서는 x 축과 y 축 모두에 `symlog` 플롯을 생성합니다. 또한 `linthresh` 매개변수를 0.015 로 설정합니다.

```python
ax2.plot(x, y3)
ax2.set_xscale('symlog')
ax2.set_yscale('symlog', linthresh=0.015)
ax2.grid()
ax2.set_ylabel('symlog both')
```

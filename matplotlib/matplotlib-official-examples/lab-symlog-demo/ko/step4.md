# x 축에 Symlog 플롯 생성

첫 번째 서브플롯에서는 x 축에 `symlog` 플롯을 생성합니다. 또한 x 축에 보조 그리드 (minor grid) 를 추가합니다.

```python
ax0.plot(x, y1)
ax0.set_xscale('symlog')
ax0.set_ylabel('symlogx')
ax0.grid()
ax0.xaxis.grid(which='minor')
```

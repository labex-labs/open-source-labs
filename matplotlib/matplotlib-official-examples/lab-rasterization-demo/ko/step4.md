# 래스터화 없이 pcolormesh 플롯 생성

래스터화와 비 (非) 래스터화의 차이점을 설명하기 위해 래스터화 없이 pcolormesh 플롯을 생성합니다.

```python
ax1.set_aspect(1)
ax1.pcolormesh(xx, yy, d)
ax1.set_title("No Rasterization")
```

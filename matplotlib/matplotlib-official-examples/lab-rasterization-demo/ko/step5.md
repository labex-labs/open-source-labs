# 래스터화가 있는 pcolormesh 플롯 생성

래스터화가 렌더링 속도를 높이고 더 작은 파일을 생성하는 방법을 설명하기 위해 래스터화가 있는 pcolormesh 플롯을 생성합니다.

```python
ax2.set_aspect(1)
ax2.set_title("Rasterization")
ax2.pcolormesh(xx, yy, d, rasterized=True)
```

# 래스터화 없이 오버레이된 텍스트가 있는 pcolormesh 플롯 생성

벡터 그래픽스가 축 및 텍스트와 같은 일부 아티스트에 대해 벡터 그래픽스의 장점을 유지할 수 있는 방법을 설명하기 위해 래스터화 없이 오버레이된 텍스트가 있는 pcolormesh 플롯을 생성합니다.

```python
ax3.set_aspect(1)
ax3.pcolormesh(xx, yy, d)
ax3.text(0.5, 0.5, "Text", alpha=0.2,
         va="center", ha="center", size=50, transform=ax3.transAxes)
ax3.set_title("No Rasterization")
```

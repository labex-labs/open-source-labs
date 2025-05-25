# RangeSlider 생성

이제 이미지의 임계값을 조정할 수 있는 RangeSlider 위젯을 생성합니다. 슬라이더 (slider) 를 위한 새로운 축 (axis) 을 생성하고 figure 에 추가합니다.

```python
slider_ax = fig.add_axes([0.20, 0.1, 0.60, 0.03])
slider = RangeSlider(slider_ax, "Threshold", img.min(), img.max())
```

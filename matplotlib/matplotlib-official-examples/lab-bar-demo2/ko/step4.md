# 막대 그래프의 x 및 y 단위 설정

이 단계에서는 다양한 키워드를 사용하여 막대 그래프의 x 및 y 단위를 설정합니다. `xunits` 및 `yunits` 매개변수를 사용하여 x 및 y 단위를 센티미터 (cm) 와 인치 (inch) 로 설정합니다.

```python
axs[0, 1].bar(cms, cms, bottom=bottom, width=width, xunits=cm, yunits=inch)
```

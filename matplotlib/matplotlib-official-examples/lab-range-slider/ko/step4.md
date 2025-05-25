# 히스토그램에 수직선 추가

임계값 설정의 효과를 더 쉽게 확인하기 위해, 현재 임계값 (threshold value) 을 나타내는 수직선 (vertical line) 을 히스토그램에 추가합니다. 하한 및 상한 임계값에 대해 각각 두 개의 선을 생성합니다.

```python
lower_limit_line = axs[1].axvline(slider.val[0], color='k')
upper_limit_line = axs[1].axvline(slider.val[1], color='k')
```

# 삽입 축 생성

이 단계에서는 `fig.add_axes`를 사용하여 메인 플롯 축 내에 두 개의 삽입 축을 생성합니다. 하나는 데이터의 히스토그램을 표시하고, 다른 하나는 임펄스 응답 (impulse response) 을 표시합니다.

```python
# Create right inset axes
right_inset_ax = fig.add_axes([.65, .6, .2, .2], facecolor='k')
right_inset_ax.hist(s, 400, density=True)
right_inset_ax.set(title='Probability', xticks=[], yticks=[])

# Create left inset axes
left_inset_ax = fig.add_axes([.2, .6, .2, .2], facecolor='k')
left_inset_ax.plot(t[:len(r)], r)
left_inset_ax.set(title='Impulse response', xlim=(0, .2), xticks=[], yticks=[])
```

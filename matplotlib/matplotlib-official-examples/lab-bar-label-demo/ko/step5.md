# `{}` 스타일 형식 문자열을 사용한 막대 레이블 지정

이 단계에서는 `{}` 스타일 형식 문자열을 사용하여 막대 레이블을 형식화하는 방법을 보여줍니다. 맛별 젤라토 판매에 대한 데이터를 사용합니다.

```python
fruit_names = ['Coffee', 'Salted Caramel', 'Pistachio']
fruit_counts = [4000, 2000, 7000]

fig, ax = plt.subplots()
bar_container = ax.bar(fruit_names, fruit_counts)
ax.set(ylabel='pints sold', title='Gelato sales by flavor', ylim=(0, 8000))
ax.bar_label(bar_container, fmt='{:,.0f}')
```
